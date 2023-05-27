from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .serializers import PersonSerializer
from .models import Person
# Create your views here.


class PersonViewSet(viewsets.ViewSet):
    serializer_class = PersonSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)