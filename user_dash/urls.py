from django.urls import path
from .views import user_dashboard_view, test_view, test_history_view, get_pre_questions, test_image_scanner, profile_view

urlpatterns = [
    path('', user_dashboard_view, name='dashboard'),
    path('start_test/', test_view, name='start_test'),
    path('tests/', test_history_view, name="user_tests"),
    path('tests/onboarding/pre-questions/', get_pre_questions, name='get_pre_questions'),
    path('tests/onboarding/image-scanner',test_image_scanner, name='test_image_scanner' ),
    path('profile/', profile_view, name='user_profile'),
]