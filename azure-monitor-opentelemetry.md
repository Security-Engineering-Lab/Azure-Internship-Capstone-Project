


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
3) Connection strings in Application Insights, https://learn.microsoft.com/en-us/azure/azure-monitor/app/connection-strings


---------------------------------------------------------------------------------------------------------------------------------------------------------

# Setting Up Azure Application Insights for Django Web Application

## Step-by-Step Process Overview

Based on the provided images, here's a comprehensive walkthrough of how to set up and integrate Azure Application Insights with a Django web application:

## 1. Creating a New Application Insights Resource

As shown in Image 1, the process begins with creating a new Application Insights resource:

- **Navigate to**: Home > Monitor | Applications > Application Insights
- **Resource Configuration**:
  - Subscription: Azure subscription 1
  - Resource Group: msdocs-django-postgres-tutorial-1
  - Name: DjangoWebApp_ApplicationInsights (highlighted in red box)
  - Region: (Europe) West Europe
  - Log Analytics Workspace: DefaultWorkspace with unique identifier

This configuration step establishes the monitoring service that will collect and analyze your Django application's telemetry data.

## 2. Resource Validation and Creation

Image 2 shows the validation and confirmation step:

- All configuration parameters are reviewed
- The system performs validation checks (shown as "Validation passed")
- Details of the configured resource are displayed:
  - Application Insights by Microsoft
  - Resource specifications matching those entered in step 1
- To complete the setup, click the "Create" button (highlighted in red)

## 3. Deployment Confirmation

Image 3 displays the deployment completion screen:

- A success message: "Your deployment is complete"
- Deployment details including:
  - Deployment name: Microsoft.AppInsights
  - Start time: 5/17/2025, 8:24:59 AM
  - Correlation ID: 2a774b94-6b1d-4eb2-bedf-9820b2011457
- Resources successfully deployed:
  - DjangoWebApp_ApplicationInsights
  - newWorkspaceTemplate
- A "Go to resource" button to access the newly created resource

## 4. Application Insights Dashboard

Image 4 shows the Application Insights dashboard for the Django application:

- The resource overview page displays essential monitoring metrics
- Key information highlighted includes:
  - **Connection String** (highlighted in red): This is critical for integrating with your Django application
  - **Instrumentation Key**: 255bXXXX-XXXX-XXXX-XXXX-41b283997035
- Dashboard panels showing:
  - Failed requests
  - Server response time
  - Server requests
  - Availability metrics
- Time range filter options (30 minutes to 30 days)

## Implementation in Django

To integrate this Application Insights resource with your Django project:

1. Copy the Connection String highlighted in Image 4
2. Add it to your Django application's environment variables:
   ```bash
   APPLICATIONINSIGHTS_CONNECTION_STRING="InstrumentationKey=255b5d65-4b45-498c-b124-41b283997035;IngestionEndpoint=..."
   ```
3. Modify your `wsgi.py` file to include:
   ```python
   import os
   from django.core.wsgi import get_wsgi_application
   from azure.monitor.opentelemetry import configure_azure_monitor

   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourproject.settings')

   if os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING"):
       configure_azure_monitor()

   application = get_wsgi_application()
   ```

Once integrated, your Django application will send telemetry data to Azure Application Insights, allowing you to monitor performance, track usage, and diagnose issues through the dashboard shown in Image 4.
