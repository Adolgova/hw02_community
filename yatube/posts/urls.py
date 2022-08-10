"""yatube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# posts/urls.py
from django.urls import path

from . import views

# Эта строчка обязательна. 
# Без неё namespace работать не будет:
# namespace должен быть объявлен при include в корневом urls.py и тут, в app_name, тот же namespace
app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Cтраницы с информацией о посте
    path('group/<slug:slug>', views.group_posts, name='group_list'),
]