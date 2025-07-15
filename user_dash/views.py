from django.http import HttpResponse
from accounts.decorators import role_required

@role_required(['user'])  # Assuming 'admin' is another role you want to allow
def dashboard_view(request):
    return HttpResponse("<html><body><h1>Hello, User!</h1></body></html>")
