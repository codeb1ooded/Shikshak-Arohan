
from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^home/', views.index),
    url(r'^signUp/', views.createUser),
    url(r'^login/', views.loginUser),
    url(r'^verify/', views.verifyUser),
    url(r'^logout/', views.logoutUser),
    url(r'^submitResume/', views.registerUserResume),
]
