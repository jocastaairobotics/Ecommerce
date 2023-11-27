from django.urls import path
from .views import LoginView, UserLoginView

urlpatterns = [
    path("", LoginView.as_view(), name='LoginView'),
    path("login", UserLoginView.as_view(), name='UserLoginView')
]