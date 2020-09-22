from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate

from root.models.UserModel import Users
from root.models.ContentModel import Content
from root.models.CourseModel import Course
from root.models.SubscriptionModel import Subscription
from root.models.Review import Review
from root.models.CategoryModel import Category

def adminhomeroute(request):
	return render(request,'adminhomeroute.html')

#127.0.0.1:8000/adminarea/

def adminlogin(request):
	auname=request.POST['auname']
	aupass=request.POST['aupass']
	user=authenticate(username=auname, password=aupass)
	data={}
	if user:
		if user.is_staff == 1 or user.is_superuser ==1:
			request.session['user']=user.id
			request.session['username']=user.username
			users=Users.objects.all()
			category=Category.objects.all()
			content=Content.objects.all()
			courses=Course.objects.all()
			data['users']=users
			data['category']=category
			data['content']=content
			data['courses']=courses
			return render(request,'adminhome.html',data)
	else:
		return HttpResponse('usernot found')

def users(request):
	if 'user' in request.session:
		users=Users.objects.all()
		return render(request,'users.html',{'data':users})

def courses(request):
	if 'user' in request.session:
		courses=Course.objects.all()
		return render(request,'courses.html',{'data':courses})

def content(request):
	if 'user' in request.session:
		content=Content.objects.all()
		return render(request,'content.html',{'data':content})


def addnewadmincontent(request):
	return render(request,'addnewadmincontent.html')

def editadmincontent(request,id):
	content=Content.objects.filter(id=id)
	return render(request,'editadmincontent.html',{'data':content})

#Remove code repetition by combining them	
def saveeditcontent(request,id):
	content=Content.objects.filter(id=id)
	if request.method == 'POST':
		newheading=request.POST['nch']
		newurl=request.POST['ncu']
		newbody=request.POST['ncb']

		for x in content:
			x.contentheading= newheading
			x.contenturl = newurl
			x.contentbody= newbody
		x.save()
		
	return HttpResponse('<script>alert("Data updated successfully" )</script>')	




def logout(request):
    request.session.flush()