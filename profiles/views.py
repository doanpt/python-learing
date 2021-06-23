# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import TemplateView


class SiteLoginView(LoginView):
    template_name = "login.html"


class SiteProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

# @login_required
# def edit_profile_view(request):
#     return render(request, 'profile.html', {})
