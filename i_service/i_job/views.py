from django.shortcuts import render
from .models import Job
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.serializers import ModelSerializer


class JobSerializer(ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, ]
