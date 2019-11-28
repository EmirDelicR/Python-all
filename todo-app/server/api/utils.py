from rest_framework.views import status
from rest_framework.response import Response
from django.db import connection
from pprint import pprint 

def make_error_response(pk):
    return Response(
        data={
			'error': True,
            "message": "Todo with id: {} does not exist".format(pk)
        },
        status=status.HTTP_404_NOT_FOUND
    )

def make_data_for_response(data, err, msg):
	return {
		'data': data,
		'error': err,
		'message': msg
	},

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

def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n\n'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )

class Formatter(object):
	"""Formatter Class 
	
	To use: 
		pretty = Formatter()
		data = pretty.format_dict(dict)
		print(data)

	To register new format: 	
		from collections import OrderedDict
		pretty.set_formater(OrderedDict, format_ordereddict)
	"""
	def __init__(self):
		self.types = {}
		self.htchar = '\t' # tab indent
		self.lfchar = '\n' # new line
		self.indent = 0

		self.set_formater(object, self.__class__.format_object)
		self.set_formater(dict, self.__class__.format_dict)
		self.set_formater(list, self.__class__.format_list)
		self.set_formater(tuple, self.__class__.format_tuple)

	def set_formater(self, obj, callback):
		self.types[obj] = callback

	def __call__(self, value, **args):
		for key in args:
			setattr(self, key, args[key])

		formater = self.types[type(value) if type(value) in self.types else object]
		return formater(self, value, self.indent)

	def format_object(self, value, indent=0):
		return repr(value)

	def format_dict(self, value, indent=0):
		items = [
			self.lfchar + self.htchar * (indent + 1) + repr(key) + ': ' +
			(self.types[type(value[key]) if type(value[key]) in self.types else object])(self, value[key], indent + 1)
			for key in value
		]
		return '{%s}' % (','.join(items) + self.lfchar + self.htchar * indent)

	def format_list(self, value, indent=0):
		items = [
			self.lfchar + self.htchar * (indent + 1) + (self.types[type(item) if type(item) in self.types else object])(self, item, indent + 1)
			for item in value
		]
		return '[%s]' % (','.join(items) + self.lfchar + self.htchar * indent)

	def format_tuple(self, value, indent=0):
		items = [
			self.lfchar + self.htchar * (indent + 1) + (self.types[type(item) if type(item) in self.types else object])(self, item, indent + 1)
			for item in value
		]
		return '(%s)' % (','.join(items) + self.lfchar + self.htchar * indent)

	def format_ordereddict(self, value, indent=0):
		items = [
			self.lfchar + self.htchar * (indent + 1) + "(" + repr(key) + ', ' + 
			(self.types[type(value[key]) if type(value[key]) in self.types else object])(self, value[key], indent + 1) + ")"
			for key in value
		]
		return 'OrderedDict([%s])' % (','.join(items) + self.lfchar + self.htchar * indent) 
		
	def preatty_print(self, value):
		print('######################## DATA ##############################')
		print(value)
		print('############################################################')
