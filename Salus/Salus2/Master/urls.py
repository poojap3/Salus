from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views
from User.views import *





app_name = 'Master'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    ]
