"""vnegg_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from courses import views
from profiles import views as profiles_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('account/', include('django.contrib.auth.urls')),
    path('login/', profiles_views.SiteLoginView.as_view(), name='login'),
    path('register/', profiles_views.SiteRegisterView.as_view(), name='register'),
    path('register_ok/', profiles_views.SiteRegisterOkeView.as_view(), name='register_ok'),
    path('logout/', profiles_views.SiteLogoutView.as_view(), name='logout'),
    path('profile/', profiles_views.ProfileEditView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
