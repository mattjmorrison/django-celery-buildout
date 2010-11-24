from django.http import HttpResponse
from blog.tasks import MyTask

def foo(request):

    if 'data' in request.REQUEST:
        MyTask.delay(some_arg=request.REQUEST['data'])

    return HttpResponse("""
        <form action="">
            <input type="text" name="data" />
            <input type="submit" />
        </form>
        """)