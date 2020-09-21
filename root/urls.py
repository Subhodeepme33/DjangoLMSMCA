from django.urls import path,include,re_path
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.home),
    path('userhome',views.userhome),   
    path('uploadprofilepic',views.profilepicchange),
    path('content/viewavailablecontents',views.viewavailablecontents),
    path('ratings',views.ratings),
    path('showchart',views.showchart,name='showchart'),
    path('myenrollments',views.showenrollments),
    re_path(r'^myprofile/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.profiledetails,name='myprofileshow'),
    re_path(r'^editprofile/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.editprofile,name='editprofile'),
    re_path(r'^enrollcourse/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.enrollcourse,name='enrollcourse'),
    re_path(r'^mycontentshow/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.mycontentshow,name='mycontentshow'),
    re_path(r'^deletecontent/(?P<id>\w+)', views.deletecontent,name='deletecontent'),
    path('register',views.register),
    path('logout',views.logout),
]
