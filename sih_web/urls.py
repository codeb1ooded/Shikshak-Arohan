"""sih_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from api.views import *

# Add this import
from django.contrib.auth import views
from login.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('login.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'^home/$', views.logout, {'template_name': 'home.html'}),

    # urls for api
    url(r'^api/create/', createUser),
    url(r'^api/signup/', signupUser),
    url(r'^api/login/', loginUser),
    url(r'^api/verify/', verifyUser),
    url(r'^api/logout/', logoutUser),
    url(r'^api/markattendance/', markAttendance),
]
