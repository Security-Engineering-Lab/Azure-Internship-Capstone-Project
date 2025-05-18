

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

# Project Folder Structure Description

## Root Directory

```
msdocs-django-postgresql-sample-app/
```

This is the main repository containing the Django application with PostgreSQL integration for Azure.

## Core Directories

### `.devcontainer/`
Contains configuration files for the development container environment, making it easier to set up a consistent development environment across different machines. This includes:
- Docker configuration
- VS Code settings
- Development dependencies

### `.github/`
Contains GitHub-specific files:
- Workflow definitions for GitHub Actions
- Issue templates
- Pull request templates

### `azureproject/`
Contains Azure-specific configuration files:
- `production.py` - Settings specific to the production environment on Azure
- Azure deployment configuration
- Environment variables handling

### `restaurant_review/`
The main Django application directory:
- `models.py` - Database models for restaurants, reviews, etc.
- `views.py` - Controller logic for handling requests
- `urls.py` - URL routing configurations
- `forms.py` - Form definitions
- `admin.py` - Admin interface configurations

### `static/`
Contains static assets for the web application:
- CSS files
- JavaScript files
- Images and other media

### `templates/`
Contains HTML templates used by the Django application:
- Base templates with shared layouts
- View-specific templates
- Partial templates/components

### `migrations/`
Contains database migration files that track changes to the models and database schema.

## Key Files

### `manage.py`
The Django command-line utility that allows performing various administrative tasks.

### `requirements.txt`
Lists all Python package dependencies including:
- Django
- psycopg2-binary (PostgreSQL adapter)
- python-dotenv
- whitenoise (static file serving)
- django-redis

### `Dockerfile`
Contains instructions for building the Docker container for the application.

### `.env.sample`
A template file showing the required environment variables that need to be configured.

### `azd.yaml`
Azure Developer CLI configuration file for streamlined Azure deployments.

## Deployment Files

### `infra/`
Contains infrastructure-as-code files for deploying to Azure:
- Bicep/ARM templates
- Environment configuration
- Resource definitions

### `scripts/`
Contains utility scripts for:
- Deployment automation
- Database migrations
- Initial data seeding
- Development environment setup

## Application Structure

The project follows Django's MVT (Model-View-Template) architecture:

1. **Models** - Define data structures and database schema
2. **Views** - Handle request processing and business logic
3. **Templates** - Define the HTML presentation
4. **URLs** - Map URLs to view functions

The application is designed to seamlessly integrate with Azure services including App Service, PostgreSQL, and Redis Cache, demonstrating a complete cloud-native web application architecture.


### References:

1) Streamlining Azure Django Deployment, https://pieces.app/blog/streamlining-azure-django-deployment
2) Deploy Django App on Azure #1: Changing Django Code for Deployment, https://www.youtube.com/watch?v=QjEVmQ4rcWA
3) Deploy Django App on Azure #2: Pushing our Code to GitHub with Git, https://www.youtube.com/watch?v=X2eUFKrY00Y
4) Deploy Django App on Azure #3: Creating Microsoft Azure Resources, https://www.youtube.com/watch?v=_Gx30E3r1xk
5) Deploy Django App on Azure #4: Deploying our Code on the Azure Portal, https://www.youtube.com/watch?v=L5oCPVr7l4c
6) Deploying Django & React App on Microsoft Azure #1: Overview and Architecture of the Deployment, https://www.youtube.com/watch?v=4Hk_wKCsRo0
7) Deploying Django & React App on Microsoft Azure #2: Changing Python Django Code for Deployment, https://www.youtube.com/watch?v=iG6HUlz1fZQ
8) Deploying Django & React App on Microsoft Azure #3: Pushing the Source Code to GitHub using Git, https://www.youtube.com/watch?v=CBUq442T-Wc
9) Deploying Django & React App on Microsoft Azure #4: Deploy Python Django Code on Microsoft Azure, https://www.youtube.com/watch?v=K15Q5fVYHN8
10) Deploying Django & React App on Microsoft Azure #5: Deploy a Vite React JS App on Microsoft Azure, https://www.youtube.com/watch?v=LZdAvNDMvIU
11) Deploying Django & React App on Microsoft Azure #6: Costs of Deployment and Troubleshooting, https://www.youtube.com/watch?v=k8zNgbkXFew
12) Project code, https://github.com/NickMol/Django-React-Deploy-Tutorial
   

- Python's Role in Accelerating Web Application Development with Django, June 2024International Research Journal on Advanced Engineering and Management (IRJAEM) 2(06):1902-1915, https://www.researchgate.net/publication/381969758_Python's_Role_in_Accelerating_Web_Application_Development_with_Django
- Management of Django Web Development in Python July 2021Journal of Management and Service Science (JMSS) 1(2):1-17, https://www.researchgate.net/publication/356292312_Management_of_Django_Web_Development_in_Python
- A Web-Based Application for Data Collection and Report Generation Using Django, https://www.researchgate.net/publication/357567540_A_Web-Based_Application_for_Data_Collection_and_Report_Generation_Using_Django
- DJANGO AS SECURE WEB-FRAMEWORK IN PRACTICE, https://www.researchgate.net/publication/354932133_DJANGO_AS_SECURE_WEB-FRAMEWORK_IN_PRACTICE
- Simulation data exchange - web interface for CostGlue application, https://www.researchgate.net/figure/The-architecture-of-a-Django-web-application_fig1_297264757
- An INTRANET-Based Web Application for College Management System Using Python with Django Web Framework, https://www.researchgate.net/publication/368719592_An_INTRANET-Based_Web_Application_for_College_Management_System_Using_Python_with_Django_Web_Framework
- Porting a Python Application to the Web Using Django: A Case Study of an Archaeological Image Processing System, https://www.researchgate.net/publication/384380230_Po, rting_a_Python_Application_to_the_Web_Using_Django_A_Case_Study_of_an_Archaeological_Image_Processing_System
- Django, a web framework using Python: tutorial presentation, https://www.researchgate.net/publication/262295717_Django_a_web_framework_using_Python_tutorial_presentation
- Python & Django the Fastest Growing Web Development Technology, https://www.researchgate.net/publication/379518425_Python_Django_the_Fastest_Growing_Web_Development_Technology
- Analysis of Python web development applications based on the Django framework, https://www.researchgate.net/publication/382400128_Analysis_of_Python_web_development_applications_based_on_the_Django_framework
- Social Media Website with Python using Django, https://www.researchgate.net/publication/382167867_Social_Media_Website_with_Python_using_Django
- Django: Developing web using Python, https://www.researchgate.net/publication/372609819_Django_Developing_web_using_Python
- Role of Python in Rapid Web Application Development Using Django, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4751833
- Introduction to Django, https://www.researchgate.net/publication/313937797_Introduction_to_Django
- A Generic Review of Web Technology: DJango and Flask, https://www.researchgate.net/publication/367619078_A_Generic_Review_of_Web_Technology_DJango_and_Flask
- Enhancing data protection in a web application using Django, https://www.researchgate.net/publication/384475477_Enhancing_data_protection_in_a_web_application_using_Django
- LlaMA2 and Django Web Application Approach for Simplifying Table Parsing: Review, https://www.researchgate.net/publication/387425253_LlaMA2_and_Django_Web_Application_Approach_for_Simplifying_Table_Parsing_Review
- Starting with Django, https://www.researchgate.net/publication/347626814_Starting_with_Django
  


