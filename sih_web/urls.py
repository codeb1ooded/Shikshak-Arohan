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
from login.views import *

from django.contrib.auth import views
from login.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    url(r'^home/$', views.logout, {'template_name': 'home.html'}),

    url(r'^$', home, name='home'),
    url(r'^mapcountry/$', map_country_function),
    url(r'^mapstate/$', map_state_function),
    url(r'^mapdistrict/$', map_district_function),
    url(r'^mapcity/$', map_city_function),

    url(r'^testmap/$', test_map),
    url(r'^dummy/$', dummy),

    url(r'^school/$', AddSchool),
    # urls for api
    url(r'^api/create/', createUser),
    url(r'^api/update/', updateUserDetails),
    url(r'^api/signup/', signupUser),
    url(r'^api/login/', loginUser),
    url(r'^api/verify/', verifyUser),
    url(r'^api/logout/', logoutUser),
    url(r'^api/markattendance/', markAttendance),
    url(r'^api/isschooladded/', isSchoolAdded),
    url(r'^api/addschool/', addSchoolToUser),
    url(r'^api/latlong/', getLatLong),
    url(r'^api/presentholidays/', getPresentAndHolidays)
]
