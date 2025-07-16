from django.http import HttpResponse
from accounts.decorators import role_required
# import render
from django.shortcuts import render

@role_required(['user'])  # Assuming 'admin' is another role you want to allow
def dashboard_view(request):
    return render(request, 'user_dash/index.html', {'user': request.user})

def test_view(request):
    return render(request, 'user_dash/test.html')

def test_history_view(request):
    return HttpResponse("This is the test history view for user dashboard.")

# On-boarding views
def get_pre_questions(request):
    with open("user_dash/pre_questions.json", "r") as file:
        pre_questions = file.read()
    # Return Json response
    return HttpResponse(pre_questions, content_type="application/json")