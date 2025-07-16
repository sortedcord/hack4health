from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.decorators import role_required
import json
# import render
from django.shortcuts import render
from .models import TestReport
import uuid
import requests
import base64

@role_required(['user'])  # Assuming 'admin' is another role you want to allow
def user_dashboard_view(request):
    return render(request, 'user_dash/index.html', {'user': request.user})

def test_view(request):
    return render(request, 'user_dash/test.html')

def test_history_view(request):
    return HttpResponse("This is the test history view for user dashboard.")

def profile_view(request):
    user_profile = request.user.userprofile
    return render(request, 'user_dash/profile.html', {'profile': user_profile})

@csrf_exempt  # If you're POSTing via JS fetch and not using a CSRF token (though it's better to include it)
def get_pre_questions(request):
    if request.method == 'POST':
        try:
            # Parse JSON input
            data = json.loads(request.body)
            answers = data.get('answers', [])

            # Create a new TestReport linked to the logged-in user
            new_test = TestReport.objects.create(
                user=request.user,
                test_id=f"PRE-{request.user.id}-{TestReport.objects.count() + 1}",
                test_data={"pre_questions": answers}
            )
            new_test.save()

            return JsonResponse({"message": "Pre-question responses saved", "test_id": new_test.test_id}, status=201)

        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)}, status=400)


    with open("user_dash/pre_questions.json", "r") as file:
        pre_questions = file.read()
    # Return Json response
    return HttpResponse(pre_questions, content_type="application/json")

def send_request_to_ml_pipeline(test_report: TestReport):
    ml_pipeline_url = "http://10.17.164.71:5000/predict"

    if not test_report.image:
        raise ValueError("No image in TestReport.")
    image_file = test_report.image

    # Read and encode as base64
    image_b64 = base64.b64encode(image_file.read()).decode('utf-8')
    payload = {"image": image_b64}

    resp = requests.post(
        ml_pipeline_url,
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"}
    )
    return resp.json()

def test_image_scanner(request):
    # if post request
    if request.method == 'POST':
        # Handle file upload
        uploaded_file = request.FILES.get('image')
        if uploaded_file:
            test_id = request.POST.get('test_id')
            test_report = TestReport.objects.get(test_id=test_id)
            image_name = str(uuid.uuid4()) + ".jpg"
            test_report.image.save(image_name, uploaded_file)
            test_report.save()
            # Save the image to the test report
            send_request_to_ml_pipeline(test_report)
            return JsonResponse({"message": "Image uploaded successfully"}, status=201)

    test_id = request.GET.get('test_id')
    test_report = TestReport.objects.get(test_id=test_id)
    
    # Send report at 192.168.1.7:5000
    
    return render(request, 'user_dash/test_image_scanner.html', {'test_id': test_report.test_id})