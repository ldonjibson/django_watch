******************************************************************
Django Watch Bugging is used to monitor the VBP application usages
******************************************************************

Django Watch Bugging is used to monitor the VBP application usage

Detailed documentation is in the "docs" directory.

Quick start
-----------
1. pip install requests 
  pip install django_watch_bugging

2a. Add "django_watch_bugging" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_watch_bugging',
    ]
2b. Add "django_watch_bugging.middleware.CheckLiValueMiddleware" to your MIDDLEWARE_CLASSES

3. Include the polls URLconf in your project urls.py like this::

    path('users/django_watch/', include('django_watch_bugging.urls')),

4. Run ``python manage.py migrate`` to create the django_watch_bugging models.

5. Start the development server and visit http://127.0.0.1:8000/admin/