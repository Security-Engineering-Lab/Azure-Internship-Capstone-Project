# generate_400_errors.py
# cd c:/Projects/DevOpsTestingStation
# python generate_400_errors.py https://msdocs-python-postgres-235-cmb4dccwfbf7emhx.westeurope-01.azurewebsites.net --iterations 200 --concurrency 10
import requests
import time
import random
import argparse
import concurrent.futures
from datetime import datetime

def send_malformed_request(url, endpoint=None, error_type="param"):
    """
    Send a deliberately malformed request to generate 400 errors
    
    error_type options:
    - "param": Send invalid query parameters
    - "header": Send malformed headers
    - "method": Use invalid HTTP methods
    - "url": Generate malformed URLs
    - "random": Randomly choose from the above
    """
    if error_type == "random":
        error_type = random.choice(["param", "header", "method", "url"])
    
    if endpoint is None:
        endpoints = [
            "",  # Root path
            "api/data",
            "users",
            "search",
            "login"
        ]
        endpoint = random.choice(endpoints)
    
    full_url = f"{url.rstrip('/')}/{endpoint.lstrip('/')}"
    
    try:
        response = None
        
        if error_type == "param":
            # Malformed parameters
            invalid_params = {
                # Invalid parameter formats
                'id': "'; DROP TABLE users; --",
                'filter': "{{$ne: null}}",
                'page': "not_a_number",
                'limit': "-50",
                # Overly long parameters
                'q': 'a' * 10000,
                # Invalid data types
                'date': "not-a-date",
                # Special characters
                'name': "test\u0000null\u0000byte",
                # SQL injection attempts that should be caught
                'query': "1=1; SELECT * FROM users"
            }
            
            # Select a random subset of parameters
            params_to_use = {k: invalid_params[k] for k in 
                           random.sample(list(invalid_params.keys()), 
                                        k=random.randint(1, 3))}
            
            response = requests.get(full_url, params=params_to_use, timeout=5)
            
        elif error_type == "header":
            # Malformed headers
            invalid_headers = {
                # Invalid content types
                'Content-Type': random.choice([
                    'invalid/content-type',
                    'application/json; charset="malformed',
                    'text/html" onerror="alert(1)',
                ]),
                # Invalid Accept headers
                'Accept': random.choice([
                    'invalid/accept-type',
                    '*/*; q=1.1',  # Invalid quality value
                    'text/html; level=9999',  # Invalid parameter
                ]),
                # Overly long headers
                'X-Custom-Header': 'x' * 8192,
                # Malformed authentication
                'Authorization': random.choice([
                    'Basic not_base64_encoded',
                    'Bearer incomplete_token',
                    'malformed auth',
                ]),
                # Invalid cookies
                'Cookie': random.choice([
                    'session={"json":"malformed}',
                    'id=123; user=test\u0000null',
                ]),
            }
            
            # Select a random subset of headers
            headers_to_use = {k: invalid_headers[k] for k in 
                            random.sample(list(invalid_headers.keys()), 
                                         k=random.randint(1, 3))}
            
            response = requests.get(full_url, headers=headers_to_use, timeout=5)
            
        elif error_type == "method":
            # Invalid HTTP methods
            invalid_methods = [
                'INVALID',
                'HACK',
                'CUSTOM',
                'TEST'
            ]
            
            method = random.choice(invalid_methods)
            response = requests.request(method, full_url, timeout=5)
            
        elif error_type == "url":
            # Malformed URLs
            malformed_urls = [
                f"{url}/{endpoint}/%00null",
                f"{url}/{endpoint}/../../etc/passwd",
                f"{url}/{endpoint}/<script>alert(1)</script>",
                f"{url}/{endpoint}/user/{{$ne:1}}",
                f"{url}/{endpoint}/test?param=value&param=duplicate", # Duplicate param
                f"{url}/{endpoint}/%u0000",  # Encoded null byte
                f"{url}/{endpoint}/{'a' * 2000}", # Overly long URL
                f"{url}/{endpoint}/test;exec=bash",  # Path parameter injection
            ]
            
            malformed_url = random.choice(malformed_urls)
            response = requests.get(malformed_url, timeout=5)
        
        if response:
            return {
                'url': response.url,
                'method': response.request.method,
                'status_code': response.status_code,
                'time': response.elapsed.total_seconds(),
                'error_type': error_type,
                'is_400': 400 <= response.status_code < 500,
                'is_500': 500 <= response.status_code < 600,
                'content_length': len(response.content) if response.content else 0
            }
        
    except requests.exceptions.RequestException as e:
        return {
            'url': full_url,
            'method': 'GET',
            'status_code': 0,
            'time': 0,
            'error_type': error_type,
            'is_400': False,
            'is_500': False,
            'error': str(e)
        }
    
    # Default return if no response
    return {
        'url': full_url,
        'method': 'GET',
        'status_code': 0,
        'time': 0,
        'error_type': error_type,
        'is_400': False,
        'is_500': False,
        'error': 'No response'
    }

def generate_400_errors(url, iterations=100, concurrency=5, delay=0.2, error_types=None):
    """Generate multiple 400 Bad Request errors"""
    
    if error_types is None:
        error_types = ["param", "header", "method", "url", "random"]
    
    results = {
        'total': 0,
        '400_errors': 0,
        '500_errors': 0,
        'other': 0,
        'by_type': {
            'param': 0,
            'header': 0,
            'method': 0,
            'url': 0
        }
    }
    
    print(f"Starting 400 error generation against {url}")
    print(f"Iterations: {iterations}")
    print(f"Concurrency: {concurrency}")
    print(f"Error types: {', '.join(error_types)}")
    print("-" * 60)
    
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = []
        
        for _ in range(iterations):
            error_type = random.choice(error_types)
            futures.append(executor.submit(send_malformed_request, url, None, error_type))
            time.sleep(delay)  # Small delay between submissions
        
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            results['total'] += 1
            
            try:
                result = future.result()
                
                if result['is_400']:
                    results['400_errors'] += 1
                    et = result['error_type']
                    if et in results['by_type']:
                        results['by_type'][et] += 1
                elif result['is_500']:
                    results['500_errors'] += 1
                else:
                    results['other'] += 1
                
                # Print progress
                if (i + 1) % 10 == 0 or i == len(futures) - 1:
                    elapsed = time.time() - start_time
                    rate = (i + 1) / elapsed
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                          f"Progress: {i+1}/{len(futures)}, "
                          f"400 Errors: {results['400_errors']}, "
                          f"Rate: {rate:.2f} req/s")
                
                # Detailed logging for some requests
                if random.random() < 0.1:  # Log about 10% of requests
                    status = result['status_code']
                    method = result['method']
                    error_type = result['error_type']
                    url = result['url']
                    
                    print(f"  Request: {method} {url}")
                    print(f"  Status: {status}, Type: {error_type}")
                    if 'error' in result:
                        print(f"  Error: {result['error']}")
                    print()
                
            except Exception as e:
                print(f"Error processing result: {e}")
    
    # Calculate final statistics
    elapsed_time = time.time() - start_time
    
    print("\n" + "=" * 60)
    print("HTTP 400 Error Generation Results:")
    print(f"Total Requests: {results['total']}")
    print(f"400 Bad Request Errors: {results['400_errors']} ({results['400_errors']/results['total']*100:.2f}%)")
    print(f"500 Server Errors: {results['500_errors']} ({results['500_errors']/results['total']*100:.2f}%)")
    print(f"Other Responses: {results['other']} ({results['other']/results['total']*100:.2f}%)")
    print("\nBy Error Type:")
    for error_type, count in results['by_type'].items():
        if count > 0:
            print(f"  {error_type}: {count} ({count/results['total']*100:.2f}%)")
    
    print(f"\nTotal Time: {elapsed_time:.2f} seconds")
    print(f"Average Rate: {results['total']/elapsed_time:.2f} requests/second")
    print("=" * 60)
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate HTTP 400 Bad Request Errors")
    parser.add_argument("url", help="Target URL of the application")
    parser.add_argument("--iterations", type=int, default=100, 
                        help="Number of requests to send")
    parser.add_argument("--concurrency", type=int, default=5, 
                        help="Number of concurrent requests")
    parser.add_argument("--delay", type=float, default=0.2, 
                        help="Delay between requests in seconds")
    parser.add_argument("--types", type=str, default="param,header,method,url,random",
                        help="Comma-separated list of error types to generate")
    

    args = parser.parse_args()
    error_types = [t.strip() for t in args.types.split(",")]
    
    generate_400_errors(
        args.url,
        args.iterations,
        args.concurrency,
        args.delay,
        error_types
    )