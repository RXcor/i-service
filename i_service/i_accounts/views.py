from django.shortcuts import render
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Account

# Create your views here.
class AccountSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

class AccountViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
