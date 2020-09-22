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
	path('addnewadmincontent',views.addnewadmincontent),
	re_path(r'^editadmincontent/(?P<id>\w+)', views.editadmincontent,name='editadmincontent'),
	
	re_path(r'^saveeditcontent/(?P<id>\w+)', views.saveeditcontent,name='saveeditcontent'),

	#re_path(r'^addnewadmincontent/(?P<id>\w+)', views.addnewadmincontent,name='addnewadmincontent'),

	path('logout',views.logout),
]