from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todoapp.models import Todo
from todoapp.serializer import TodoSerializer


@api_view(['GET','POST'])
def todo_list(request):
    if request.method=='GET':
        todo=Todo.objects.all()
        serializer=TodoSerializer(todo,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PUT','DELETE'])
def event_details(request,id):
    try:
        events=Todo.objects.get(id=id)
    except events.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method=='GET':
        serializer=TodoSerializer(events)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=TodoSerializer(events,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        events.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









