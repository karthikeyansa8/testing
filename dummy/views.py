from dummy.serializers import TestSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import testform
# Create your views here.

class Form(APIView):
    
    def get(self, request):
        data = testform.objects.all()
        serializer = TestSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print(f"Request data: {request.data}")
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(f"Serializer Data: {serializer.validated_data}")
            return Response({"message": "Data saved successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            print("Serializer errors:", serializer.errors)
            return Response({"message": "Validation error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
