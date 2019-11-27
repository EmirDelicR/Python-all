from rest_framework import generics, viewsets
from rest_framework.views import status, APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

# Imports for data
from .models import Todo, User, Address
from .serializers import TodoSerializer, CustomLoginSerializer, AddressSerializer

# My custom imports
from .decorators import validate_request_data
from .utils import make_error_response, make_data_for_response


import json

# Create your views here.
def home(req):
    return HttpResponse("<h>This is home page</h>")


class CustomLoginView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = CustomLoginSerializer    
    
    def get(self, request):
        data = self.get_queryset()
        data = make_data_for_response(data=self.serializer_class(data, many=True).data, err=False, msg="Success")
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer = serializer_class()
        user = serializer.create(request.data)
        data = make_data_for_response(data=self.serializer_class(user).data, err=False, msg="User successfully created") 
        
        return Response(data=data, status=status.HTTP_201_CREATED)


class ListCreateTodoView(generics.ListAPIView):
    """
    GET todo/
    POST todo/
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    # The way to overwrite function
    def get(self, request):
        data = self.get_queryset()
        data = make_data_for_response(data=self.serializer_class(data, many=True).data, err=False, msg="Success")
        return Response(data=data, status=status.HTTP_200_OK)
        
    @validate_request_data
    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=request.data["userId"])
        # user = get_object_or_404(User, id=request.data["userId"])
        todo = Todo.objects.create(
            title=request.data["title"],
            task=request.data["task"],
            user=user,
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


class TestApiView(APIView):
    """
    View to list all todo in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all Todo's.
        """
        print("*************** All utils function in APIView *******************")
        print("Check allowed methods in function: ", self._allowed_methods())
        print("Check view name: ", self.get_view_name())
        print("Check throttles: ", self.check_throttles(request))
        print("Check API version: ", self.determine_version(request))

        all_todo = [todo.title for todo in Todo.objects.all()]
        data = make_data_for_response(data=all_todo, err=False, msg="ApiView GET method successfully executed")
        return Response(data=data, status=status.HTTP_200_OK)


class TestModelViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    # To overwrite list function
    # def list(self, request):
    #     print("This is list: ")

    @action(detail=True, methods=['post'])
    def set_todo(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=request.data["userId"])
            # user = get_object_or_404(User, id=request.data["userId"])
            todo = Todo.objects.create(
                title=request.data["title"],
                task=request.data["task"],
                user=user,
            )

            data = make_data_for_response(data=self.serializer_class(todo).data, err=False, msg="Todo successfully created")    
            return Response(
                data=data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestSerializerView(APIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    # get
    # serializer = AddressSerializer(data)
    # print(serializer.data)
    # serializer.is_valid(raise_exception=True)