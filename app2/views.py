from django.shortcuts import render
from django.http import JsonResponse
from .models import student
from .serializer import studentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# API Overview View
@api_view(['GET'])
def api_overview(request):
    """
    Provides an overview of the available API endpoints.
    """
    api_urls = {
        'Get All Students and create': '/students/',
        'detail delete update student': '/students/<id>/',
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])
def students_list (request, format= False):
    if request.method == 'GET':
        students = student.objects.all()
        serializer = studentSerializer(students, many = True)
        return JsonResponse ({'students_list ': serializer.data}, safe= False)
    
    if request.method == 'POST':
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response (serializer.data, status= status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def student_info (request, id, format= False):
    try:
        student_data = student.objects.get(pk = id)
    except student_data.DoseNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
    
    if request.method =='GET':
        serializer = studentSerializer(student_data)
        return Response(serializer.data)
    

    if request.method =='PUT':
        serializer = studentSerializer(student_data, data = request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    if request.method =='DELETE':
        student_data.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

