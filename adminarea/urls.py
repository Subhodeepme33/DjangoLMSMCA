from django.urls import path,include,re_path
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

urlpatterns = [
	path('',views.adminhomeroute),
	path('adminlogin',views.adminlogin),
	path('users',views.users),
	path('courses',views.courses),
	path('logout',views.logout),
]