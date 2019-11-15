from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import status
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

from .decorators import validate_request_data
from .utils import make_error_response, make_data_for_response

import json

# Create your views here.
def home(req):
    return HttpResponse("<h>This is home page</h>")


class ListCreateTodoView(generics.ListAPIView):
    """
    GET todo/
    POST todo/
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    # def get(self, request):
    #     data = self.get_queryset()
    #     data = make_data_for_response(data=json.dumps(data), err=False, msg="Success")
    #     return Response(data=data, status=status.HTTP_200_OK)
        
    # TODO Handle server side errors properly
    @validate_request_data
    def post(self, request, *args, **kwargs):
        todo = Todo.objects.create(
            title=request.data["title"],
            task=request.data["task"]
        )

        data = make_data_for_response(data=self.serializer_class(todo).data, err=False, msg="Todo successfully created")    
        return Response(
            data=data,
            status=status.HTTP_201_CREATED
        )


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        GET todo/:id/
        PUT todo/:id/
        DELETE todo/:id/
    """
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

    def get(self, request, *args, **kwargs):
       try:
           todo = self.queryset.get(id=kwargs["id"])
           data = make_data_for_response(data=self.serializer_class(todo).data, err=False, msg="Success")  
           return Response(data=data, status=status.HTTP_200_OK)
       except Todo.DoesNotExist:
           return make_error_response(kwargs["id"])

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            todo = self.queryset.get(id=kwargs["id"])
            serializer = TodoSerializer()
            updated_todo = serializer.update(todo, request.data)
            data = make_data_for_response(data=self.serializer_class(updated_todo).data, err=False, msg="Todo successfully updated")    
            return Response(data=data)
        except Todo.DoesNotExist:
            return make_error_response(kwargs["id"])

    def delete(self, request, *args, **kwargs):
        try:
            todo = self.queryset.get(id=kwargs["id"])
            data = make_data_for_response(data=self.serializer_class(todo).data, err=False, msg="Todo successfully deleted")
            todo.delete()    
            return Response(data=data, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return make_error_response(kwargs["id"])   