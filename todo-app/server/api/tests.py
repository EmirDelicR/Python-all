import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from .models import Todo
from .serializers import TodoSerializer

# Create your tests here.

class TodoModelTest(APITestCase):
    def setUp(self):
        self.todo = Todo.objects.create(
            title="Todo - 1",
            task="This is the first task"
        )

    def test_todo(self):
        """"
        This test ensures that the todo created in the setup
        exists
        """
        self.assertEqual(self.todo.title, "Todo - 1")
        self.assertEqual(self.todo.task, "This is the first task")
        self.assertEqual(str(self.todo), "Todo - 1 - This is the first task")


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_todo(title="", task="", done=False):
        if title != "" and task != "":
            Todo.objects.create(title=title, task=task, done=done)
    
    def __set_call(self, id):
        try:
            url = reverse("todo-detail", args=(), kwargs={"id": id})
            return url
        except NoReverseMatch as err:
            # do sth
            print("NoReverseMatch: {0}".format(err))

    def make_a_request(self, method="post", **kwargs):
        """
        Make a post request to create a todo
        :param method: HTTP VERB (post, get, put)
        :return:
        """
        if method == "post":
            return self.client.post(
                reverse("todo-all-create"),
                data=json.dumps(kwargs["data"]),
                content_type='application/json'
            )

        if method == "put":
            return self.client.put(
                self.__set_call(id=kwargs["id"]),
                data=json.dumps(kwargs["data"]),
                content_type='application/json'
            )

        return None        

    def fetch_a_todo(self, pk=0):
        return self.client.get(
            self.__set_call(id=pk)
        )

    def delete_a_todo(self, pk=0):
        return self.client.delete(
            self.__set_call(id=pk)
        )    

    def setUp(self):
        # add test data
        self.create_todo("Todo First", "Do some thing now")
        self.create_todo("Todo Second", "Do some thing in one hour")
        self.create_todo("Todo Third", "Do some thing in two hour's")
        self.create_todo("Todo Fourth", "Do some thing in five hour's")
        self.valid_data = {
            "title": "test todo title",
            "task": "test todo task",
            "done": False
        }
        self.invalid_data = {
            "title": "",
            "task": ""
        }
        self.invalid_todo_id = '4f95fe39-8715-467d-8039-2daaee1eae7c'


class GetAllTodoTest(BaseViewTest):

    def test_get_all_todo(self):
        """
        This test ensures that all todo's added in the setUp method
        exist when we make a GET request to the todo/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("todo-all-create")
        )
        # fetch the data from db
        expected = Todo.objects.all()
        serialized = TodoSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetASingleTodoTest(BaseViewTest):

    def test_get_a_todo(self):
        """
        This test ensures that a single todo of a given id is
        returned
        """
        valid_id = Todo.objects.all()[0].id
        # hit the API endpoint
        response = self.fetch_a_todo(valid_id)
        # fetch the data from db
        expected = Todo.objects.get(id=valid_id)
        serialized = TodoSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test with a todo that does not exist
        response = self.fetch_a_todo(self.invalid_todo_id)
        self.assertEqual(
            response.data["message"],
            "Todo with id: 4f95fe39-8715-467d-8039-2daaee1eae7c does not exist"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AddTodoTest(BaseViewTest):

    def test_create_a_todo(self):
        """
        This test ensures that a single todo can be added
        """
        # hit the API endpoint
        response = self.make_a_request(
            method="post",
            data=self.valid_data
        )
        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # test with invalid data
        response = self.make_a_request(
            method="post",
            data=self.invalid_data
        )
        self.assertEqual(
            response.data["message"],
            "Both title and task are required to add a todo"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateTodoTest(BaseViewTest):

    def test_update_a_todo(self):
        """
        This test ensures that a single todo can be updated. In this
        test we update the second todo in the db with valid data and
        the third todo with invalid data and make assertions
        """
        # hit the API endpoint
        response = self.make_a_request(
            method="put",
            id=Todo.objects.all()[1].id,
            data=self.valid_data
        )
        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test with invalid data
        response = self.make_a_request(
            method="put",
            id=Todo.objects.all()[2].id,
            data=self.invalid_data
        )
        self.assertEqual(
            response.data["message"],
            "Both title and task are required to add a todo"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteTodoTest(BaseViewTest):

    def test_delete_a_todo(self):
        """
        This test ensures that when a todo of given id can be deleted
        """
        # hit the API endpoint
        response = self.delete_a_todo(Todo.objects.all()[3].id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # test with invalid data
        response = self.delete_a_todo(self.invalid_todo_id)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)        