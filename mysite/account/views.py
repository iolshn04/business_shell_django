from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Profile


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "account/register.html"
    success_url = reverse_lazy("blog:home")

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


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse("account:login"))
