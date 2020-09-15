from django.urls import path,include,re_path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('contentcreate/',views.contentcreate),
    path('continuecreate',views.continuecreate),
    path('displaycontent',views.displaycontent),
    #path('myenrollments',views.showenrollments),
    re_path(r'^editcontent/(?P<id>\w+)', views.editcontent,name='editcontent'),
    re_path(r'^editfinal/(?P<id>\w+)', views.editfinal,name='editfinal'),
    re_path(r'^editfinish/(?P<id>\w+)', views.editfinish,name='editfinish'),
    re_path(r'^viewmycontent/(?P<id>\w+)', views.viewmycontent,name='viewmycontent'),
    re_path(r'^displaymycontent/(?P<id>\w+)', views.displaymycontent,name='displaymycontent'),
    re_path(r'^addnew/(?P<uid>[0-9a-f-]+)/$', views.addnew,name='addnew'),
    re_path(r'^showcontent/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.showcontent,name='showcontent'),
    re_path(r'^fetchcontent/(?P<id>\w+)/(?P<uid>[0-9a-f-]+)/$', views.fetchcontent,name='fetchcontent'),
    path('viewcontinuecreate',views.viewcontinuecreate),
    
 ]