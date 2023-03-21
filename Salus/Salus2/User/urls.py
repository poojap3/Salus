from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import *






app_name = 'User'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupApi.as_view(), name="SIGNUP"),
    path('login/', LoginApiView.as_view(), name='LOGIN'),

    ]
