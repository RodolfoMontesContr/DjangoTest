from .views import home
from django.urls import path, include


urlpatterns=[
    path('', home, name="home"),
    path('', include('core.urls')),
]