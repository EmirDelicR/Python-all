from rest_framework.views import status
from rest_framework.response import Response

def make_error_response(pk):
    return Response(
        data={
            "message": "Todo with id: {} does not exist".format(pk)
        },
        status=status.HTTP_404_NOT_FOUND
    )