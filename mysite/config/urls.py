"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
#추가
from pybo import views  #from 모듈 import 이름(함수이름)


urlpatterns = [
    path('admin/', admin.site.urls),
    #추가
    #path('pybo/', views.index),
    # #localhost:8000/pybo ->localhost:8000/까지 생략 가능
    # include(module)
    path('pybo/', include('pybo.urls')),
]
