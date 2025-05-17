

# Project Description: Django PostgreSQL Sample App on Azure

## Overview

The repository [msdocs-django-postgresql-sample-app](https://github.com/VitaliiShevchuk2023/msdocs-django-postgresql-sample-app.git) is a demonstration web application built with Python using the Django framework and Azure Database for PostgreSQL relational database service. The project showcases the complete development and deployment lifecycle of a web application in the Azure App Service cloud environment.

## Key Features

1. **Complete Azure Integration**:
   - Deployment in Azure App Service
   - Connection to Azure PostgreSQL database
   - Integration with Azure Redis Cache for caching

2. **Data Caching**:
   - Demonstration of Azure Redis Cache functionality
   - Caching of restaurant details page for 60 seconds

3. **Fully Configured Development Environment**:
   - Dev Container configuration for local development
   - GitHub Codespaces support
   - Ready for use with Azure Developer CLI (azd)

## Technical Stack

- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Caching**: Redis
- **Deployment**: Azure App Service
- **Additional Packages**:
  - `psycopg2-binary` - PostgreSQL driver for Python
  - `python-dotenv` - Environment variables loader
  - `whitenoise` - Static files handling in production
  - `django-redis` - Django integration with Redis

## Getting Started

### Local Development with GitHub Codespaces:

1. Fork the repository
2. Open the project in GitHub Codespaces
3. In the terminal, run:
   ```bash
   # Database migration
   python3 manage.py migrate
   
   # Start development server
   python3 manage.py runserver
   ```
4. The application will be accessible on port 8000

### Deployment to Azure with Azure Developer CLI:

1. Sign up for a free Azure account
2. Install the Azure Developer CLI
3. Initialize a new azd environment:
   ```bash
   azd init
   ```
4. Provision resources and deploy code:
   ```bash
   azd up
   ```
5. After deployment completes, you'll receive the URL of your application

6. For access to the admin panel `/admin`, you need to create a superuser:
   - Go to the Azure Portal for App Service
   - Select SSH
   - Execute the command:
     ```bash
     python3 manage.py createsuperuser
     ```

## Additional Information

This project serves as an excellent example for learning Django application development with deployment in the Azure cloud environment. It also demonstrates best practices for database integration, caching, and setting up a secure development environment.

This demonstration application is ideal for developers looking to learn about Python application deployment in the cloud and gain practical experience working with Azure App Service, PostgreSQL, and Redis.
