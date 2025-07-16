from django.urls import path
from .views import dashboard_view, test_view, test_history_view, get_pre_questions

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('start_test/', test_view, name='start_test'),
    path('tests/', test_history_view, name="user_tests"),
    path('tests/onboarding/pre-questions/', get_pre_questions, name='get_pre_questions'),
]