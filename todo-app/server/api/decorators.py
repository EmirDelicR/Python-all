
from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        title = args[0].request.data.get("title", "")
        task = args[0].request.data.get("task", "")
        if not title and not task:
            return Response(
                data={
                    "message": "Both title and task are required to add a todo"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated