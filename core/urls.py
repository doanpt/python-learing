from django.contrib import admin
from django.urls import path

from core.views import HomeView

# step to integrate a template
# 1. download a template from internet
# 2. extract the template
# 3. copy js,style, plugins and image(optional) to static/xxx folder
# 4. create a html file in template folder
# 5. create a views and setup url
# 6. in html file, add load static and using static in href

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]
