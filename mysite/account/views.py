from random import random

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Profile


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/post_detail.html"
    success_url = reverse_lazy("myauth:about-me")

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)
        return response


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("myauth:login")