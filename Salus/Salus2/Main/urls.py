from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
# from . import views
from User.views import *
from Main.views import *

app_name = 'Main'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    # path('company/', CompanyAPIView.as_view(), name ='COMPANY'),
    path('company/', CompanyAPIView.as_view(), name="SIGNUP"),

    path('studyinformation/',StudyinformationAPIView.as_view(), name='STUDYINFORMATION')
    ]
