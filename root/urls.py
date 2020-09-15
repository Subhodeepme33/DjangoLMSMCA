from django.urls import path,include,re_path
from django.conf.urls.static import static
from . import views
from django.conf.urls import url
 
urlpatterns = [
    path('',views.home),
    path('userhome',views.userhome),
    
    path('uploadprofilepic',views.profilepicchange),
    path('content/viewavailablecontents',views.viewavailablecontents),
    
    #path('content/mycourses',views.mycourses),
    re_path(r'^myprofile/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.profiledetails,name='myprofileshow'),
    re_path(r'^editprofile/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.editprofile,name='editprofile'),
    re_path(r'^enrollcourse/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.enrollcourse,name='enrollcourse'),
    re_path(r'^mycontentshow/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.mycontentshow,name='mycontentshow'),
    path('register',views.register),
    path('myenrollments',views.showenrollments),
    #url(r'^register$',views.register),
    path('logout',views.logout),
]

