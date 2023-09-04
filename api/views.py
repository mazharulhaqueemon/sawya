from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK,HTTP_204_NO_CONTENT,HTTP_201_CREATED
from rest_framework.views import APIView
from .models import student
from .serializer import studentSerializer
from rest_framework import status


def index(request):
    return HttpResponse("Hello world")


@api_view(['GET','POST','DELETE','PUT','PATCH'])
def funcbaseapiview(request, pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
 # **** this code for search single user using his id******
            stu = student.objects.get(id=id)
            serializer = studentSerializer(stu)
            return Response(serializer.data)
  #***** This code for show all data of student model
        stu = student.objects.all()
        serializer = studentSerializer(stu,many=True)
        return Response(serializer.data)

    if request.method =='POST':
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res ={'msg':'Data has been created'}
            return Response(res)
        return Response({'msg':serializer.errors})

    if request.method =='PUT':
        id = pk
        stu = student.objects.get(pk=id)
        serializer =studentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

    if request.method =='PATCH':
        id =pk
        stu = student.objects.get(pk=id)
        serializer = studentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            return Response ({'msg':'partaila data update'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id =pk
        stu = student.objects.get(pk=id)
        stu.delete()
        return Response ({'msg':'Data Deleted'})

# function base api view

class classBaseApiView(APIView):
    def get(self,request,format=None,pk=None):
        id = pk
        if id is not None:
 # **** this code for search single user using his id******
            stu = student.objects.get(id=id)
            serializer = studentSerializer(stu)
            return Response(serializer.data)
  #***** This code for show all data of student model
        stu = student.objects.all()
        serializer = studentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request,format= None):
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res ={'msg':'Data has been created'}
            return Response(res)
        return Response({'msg':serializer.errors})

    def put(self,request, pk = None):
        id = pk
        stu = student.objects.get(pk=id)
        serializer =studentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    def patch(self,request,pk):
        id =pk
        stu = student.objects.get(pk=id)
        serializer = studentSerializer(stu,data=request.data,partial=True)# partial update means any filds can be update .
        if serializer.is_valid():
            serializer.save()
            return Response ({'msg':'partaila data update'})
        return Response(serializer.errors)
    def delete(self,request,pk):
        id =pk
        stu = student.objects.get(pk=id)
        stu.delete()
        return Response ({'msg':'Data Deleted'})








