from django.http import HttpResponse
from blog.tasks import MyTask

def foo(request):
	MyTask.delay(some_arg="foo")
	return HttpResponse("Here is your page!!!")