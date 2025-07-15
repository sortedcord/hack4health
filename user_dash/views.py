from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return HttpResponse("<html><body><h1>Hello, User!</h1></body></html>")
