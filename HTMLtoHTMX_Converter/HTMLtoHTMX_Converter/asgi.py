"""
ASGI config for HTMLtoHTMX_Converter project.

This file contains the ASGI application used for serving the project.
ASGI (Asynchronous Server Gateway Interface) is the specification that allows 
for handling asynchronous requests, making it suitable for real-time features 
such as WebSockets, long-polling, and more.

This configuration is crucial for deploying the project on ASGI-compatible servers 
and enabling asynchronous features in Django.

For more information, see:
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# Import the 'os' module to interact with the operating system
import os

# Import 'get_asgi_application' to create an ASGI application instance
from django.core.asgi import get_asgi_application

# Set the default settings module for the project. This tells Django which settings to use.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HTMLtoHTMX_Converter.settings")

# Create the ASGI application instance that will be used by ASGI servers
# This application instance will serve the Django project and handle requests asynchronously
application = get_asgi_application()

"""
Deployment Context:

The ASGI application created in this file is used when deploying the project to an ASGI-compatible server. 
Common servers include Daphne and Uvicorn. These servers are capable of handling asynchronous requests, 
which is beneficial for applications that require real-time data processing.

Ensure that your deployment environment is configured to use ASGI if you plan to leverage 
real-time features or asynchronous communication.
"""

"""
References:

- Django ASGI Documentation: https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
- ASGI Documentation: https://asgi.readthedocs.io/en/latest/
- Django Channels (for WebSockets and more): https://channels.readthedocs.io/en/stable/

These resources provide additional context and guidance on using ASGI with Django.
"""
