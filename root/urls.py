from django.urls import path,include,re_path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home),
    path('login',views.login),
    path('uploadprofilepic',views.profilepicchange),
    path('content/viewavailablecontents',views.viewavailablecontents),
    re_path(r'^myprofile/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.profiledetails,name='myprofileshow'),
    re_path(r'^editprofile/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.editprofile,name='editprofile'),
    re_path(r'^enrollcourse/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.enrollcourse,name='enrollcourse'),
    re_path(r'^mycontentshow/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.mycontentshow,name='mycontentshow'),
    path('register',views.register),
    path('logout',views.logout),

]

