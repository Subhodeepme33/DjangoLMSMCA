from django.urls import path,include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home),
    path('login',views.login),
    path('uploadprofilepic',views.profilepicchange),
    path('register',views.register),
    path('logout',views.logout),

]


'''
path('login',views.login)
path('logout',views.logout),
path('about',views.about),
'''