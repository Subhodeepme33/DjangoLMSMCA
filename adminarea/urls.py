from django.urls import path,include,re_path
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

urlpatterns = [
	path('',views.adminhomeroute),
	path('adminlogin',views.adminlogin),
	path('users',views.users),
	path('courses',views.courses),
	path('content',views.content),
	path('subscription',views.subscription),
	path('comments',views.comments),
	re_path(r'^suspenduser/(?P<id>\w+)', views.suspenduser,name='suspenduser'),
	re_path(r'^activateuser/(?P<id>\w+)', views.activateuser,name='activateuser'),
	re_path(r'^deletecomment/(?P<id>\w+)', views.deletecomment,name='deletecomment'),
	re_path(r'^editadmincontent/(?P<id>\w+)', views.editadmincontent,name='editadmincontent'),
	re_path(r'^saveeditcontent/(?P<id>\w+)', views.saveeditcontent,name='saveeditcontent'),
	re_path(r'^deleteadmincontent/(?P<id>\w+)', views.deleteadmincontent,name='deleteadmincontent'),
	path('logout',views.logout),
]