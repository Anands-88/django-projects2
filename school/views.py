from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import * 

class ParentList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ContributionList(generics.ListCreateAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ContributionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
    