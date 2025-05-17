


# Integrating OpenTelemetry with Django: A Practical Approach

## 1. Introduction

OpenTelemetry is an open standard and set of tools for collecting telemetry from software applications. In this lecture, we'll explore a practical approach to integrating OpenTelemetry with Django applications, using Azure Monitor as a backend for data analysis.

## 2. Why Use OpenTelemetry?

- **Standardized Monitoring** - a unified approach to collecting metrics, traces, and logs
- **Vendor Independence** - ability to change the backend without changing instrumentation
- **Distributed Tracing** - tracking requests across different services and components
- **Automatic Instrumentation** - minimal code changes for maximum information

## 3. Migrating from OpenCensus to OpenTelemetry

OpenCensus is considered deprecated and will only be supported by Microsoft until September 30, 2024. Therefore, it is recommended to use OpenTelemetry-based solutions.

### Key Migration Steps:

1. Removing all OpenCensus libraries from the project
2. Removing OpenCensus settings from the code
3. Installing and configuring OpenTelemetry

## 4. Installing the Required Packages

```bash
# Remove deprecated OpenCensus packages
pip uninstall opencensus-ext-azure opencensus-ext-django opencensus-ext-requests opencensus-ext-logging opencensus-ext-postgresql

# Install OpenTelemetry packages
pip install azure-monitor-opentelemetry
```

## 5. Integration with Django Application

### 5.1. Removing OpenCensus from Django Settings (settings.py)

You need to remove all settings related to OpenCensus:

```python
# Remove from settings.py
MIDDLEWARE = [
    # ...
    # Remove 'opencensus.ext.django.middleware.OpencensusMiddleware',
    # ...
]

# Remove the OPENCENSUS = { ... } block
```

### 5.2. Configuring OpenTelemetry in wsgi.py

In the wsgi.py file, add Azure Monitor OpenTelemetry configuration:

```python
import os
from django.core.wsgi import get_wsgi_application

# Import Azure Monitor OpenTelemetry
from azure.monitor.opentelemetry import configure_azure_monitor

# Set default value for Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

# Configure OpenTelemetry only if the environment variable exists
if os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING"):
    configure_azure_monitor()

# Get the Django WSGI application
application = get_wsgi_application()
```

## 6. Using During Development

During local development, you can set the environment variable:

```bash
export APPLICATIONINSIGHTS_CONNECTION_STRING="InstrumentationKey=your-key-here"
```

Or add a check for the presence of the environment variable to avoid errors during local execution:

```python
if os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING"):
    configure_azure_monitor()
```

## 7. Deployment in Azure

When deploying to Azure App Service, ensure that the `APPLICATIONINSIGHTS_CONNECTION_STRING` environment variable is correctly configured in the application settings.

## 8. Types of Telemetry Collected

After configuring OpenTelemetry with Azure Monitor, your Django application will automatically collect:

- **Requests** - HTTP requests to your application, URL paths, response codes
- **Dependencies** - SQL queries to the database, API calls
- **Traces** - distributed traces across different components
- **Logs** - system and user logs

## 9. Viewing and Analyzing Telemetry

Collected data can be viewed in Azure Application Insights:

1. Go to your Application Insights resource in the Azure Portal
2. The "Monitoring" section contains the main dashboards
3. For detailed analysis, use the "Requests", "Dependencies", "Traces" sections

## 10. Additional Configuration (Optional)

OpenTelemetry allows additional instrumentation configuration, such as:

- Excluding certain URLs from tracking
- Adding custom attributes to traces
- Configuring custom event handlers

## 11. Benefits of Using Azure Monitor OpenTelemetry

- Integrates with the full Azure ecosystem
- Simplified configuration process through a single `configure_azure_monitor()` function
- Automatic tracking of SQL queries and HTTP dependencies
- No need to install and configure additional exporters

## 12. Conclusion

Integrating OpenTelemetry with Django is a simple process that provides powerful capabilities for monitoring your application's performance. It allows you to identify performance issues, track response times, and analyze user behavior.

Azure Monitor OpenTelemetry provides an easy way to integrate without the need for detailed configuration of individual components, which significantly simplifies the process for developers.
 

### References:

1) Django, Flask, FastAPI and Azure OpenTelemetry, https://www.youtube.com/watch?v=K_fn6nXHa0s
2) Azure Monitor Opentelemetry Distro client library for Python, https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/monitor/azure-monitor-opentelemetry/README.md
3) 
