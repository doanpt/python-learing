# from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView


class SiteLoginView(LoginView):
    template_name = "login.html"


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'data-id': 1000}))

    class Meta:
        model = User
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}
        # widgets = {'email': forms.EmailInput(attrs={'required': True})}


class SiteRegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'],
            password=data['password1'],
            email=data['email'])
        url = f"{reverse('register_ok')}?username={new_user.username}"
        from pprint import pprint; pprint(url)
        return redirect(url)


class SiteRegisterOkeView(TemplateView):
    template_name = 'register_ok.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context


class SiteProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"


class SiteLogoutView(LogoutView):
        template_name = "logout.html"

# @login_required
# def edit_profile_view(request):
#     return render(request, 'profile.html', {})
