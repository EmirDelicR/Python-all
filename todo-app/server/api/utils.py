from rest_framework.views import status
from rest_framework.response import Response
from django.db import connection

def make_error_response(pk):
    return Response(
        data={
            "message": "Todo with id: {} does not exist".format(pk)
        },
        status=status.HTTP_404_NOT_FOUND
    )

def test_command(arg_1, arg_2):
    print("This is {} , and this is {}".format(arg_1, arg_2))

def print_sql_queries():
	indentation = 2
	print("%s\033[33mThe number of SQL Queries is: %s \n" % (" " * indentation, len(connection.queries)))

	if len(connection.queries) > 0:
		width = 240
		total_time = 0.0
		for query in connection.queries:
			nice_sql = query['sql'].replace('"', '').replace(',', ', ')
			sql = "\033[33mTime: \033[31m [%s]\n \033[33m Query: \033[34m%s" % (query['time'], nice_sql)
			total_time = total_time + float(query['time'])
			while len(sql) > width - indentation:
				print("%s%s" % (" " * indentation, sql[:width - indentation]))
				sql = sql[width - indentation:]
			print("%s%s\n" % (" " * indentation, sql))
		replace_tuple = (" " * indentation, str(total_time))
		print("%s\033[1;32m[TOTAL TIME: %s seconds]\033[0m" % replace_tuple)