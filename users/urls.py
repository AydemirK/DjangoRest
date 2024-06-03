from django.urls import path
from users import views
from users.views import RegistrationAPIView, AuthorizationAPIView, ConfirmUserAPIView

urlpatterns = [
    # path('registration/', views.registration_api_view),
    path('registration/', RegistrationAPIView.as_view()),
    # path('authorization/', views.authorization_api_view),
    path('authorization/', AuthorizationAPIView.as_view()),
    # path('confirm/', views.confirm_user_api_view),
    path('confirm/', ConfirmUserAPIView.as_view()),
]
