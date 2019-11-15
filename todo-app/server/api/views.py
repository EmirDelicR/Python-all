from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import status
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

from .decorators import validate_request_data
from .utils import make_error_response

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
    
    # TODO Handle server side errors properly
    @validate_request_data
    def post(self, request, *args, **kwargs):
        todo = Todo.objects.create(
            title=request.data["title"],
            task=request.data["task"]
        )

        return Response(
            data=TodoSerializer(todo).data,
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
           return Response(TodoSerializer(todo).data)
       except Todo.DoesNotExist:
           return make_error_response(kwargs["id"])

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            todo = self.queryset.get(id=kwargs["id"])
            serializer = TodoSerializer()
            updated_todo = serializer.update(todo, request.data)
            return Response(TodoSerializer(updated_todo).data)
        except Todo.DoesNotExist:
            return make_error_response(kwargs["id"])

    def delete(self, request, *args, **kwargs):
        try:
            todo = self.queryset.get(id=kwargs["id"])
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Todo.DoesNotExist:
            return make_error_response(kwargs["id"])   