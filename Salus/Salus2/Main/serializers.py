from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User



class CompanySerializer(serializers.Serializer):
    
    class Meta:
        model = Company
        fields = "__all__"

\

class StudyinformationSerializer(serializers.Serializer):

    class Meta:
        model = Studyinformation
        fields = "__all__"