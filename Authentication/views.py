from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import FormView, View
from .forms import UserLoginForms, SignupForm
from django.contrib.auth import authenticate, login, logout


class LoginView(FormView):
    form_class = UserLoginForms
    template_name = "authentication/login.html"


class UserLoginView(View):

    def get(self, request):
        logout(request)
        return redirect("/")

    def post(self, request):
        data = request.POST
        user = authenticate(username=data.get("username"), password=data.get("password"))
        if user:
            login(request, user)
            return redirect("/")
        else:
            return render(request, template_name="authentication/login.html", context={"form": UserLoginForms()})


class SignupFormView(FormView):
    template_name = "authentication/signup.html"
    form_class = SignupForm


class SignUpView(View):

    def post(self, request):
        data = request.POST
        form = SignupForm(data=data)
        if form.is_valid():
            form.save()
            return redirect("/authentication/")
        else:
            ctx = {"form": form}
            return render(request, template_name="authentication/signup.html", context=ctx)
