# apps/urls.py

from django.urls import path
from .views import welcome

urlpatterns = [
    path('', welcome, name='welcome'),  # This maps the root URL to the welcome view
]
