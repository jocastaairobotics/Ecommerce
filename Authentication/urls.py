from django.urls import path
from .views import LoginView, UserLoginView, SignupFormView, SignUpView

urlpatterns = [
    path("", LoginView.as_view(), name='LoginView'),
    path("login", UserLoginView.as_view(), name='UserLoginView'),
    path("signup", SignupFormView.as_view(), name="SignupFormView"),
    path("signupview", SignUpView.as_view(), name="SignUpView")
]