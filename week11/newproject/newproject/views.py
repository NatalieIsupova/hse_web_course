from django.http import HttpResponse
from django.template.loader import render_to_string

JSONRPC_SERVER = 'https://127.0.0.1:5000'

def index(request):
	name = request.GET.get('username', 'world')

	res = jsonrpcclient.method()
	
	return HttpResponse(render_to_string('index.html', {'username': name}))