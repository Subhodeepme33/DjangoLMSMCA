from django.shortcuts import render,redirect
from .models.UserModel import Users
from .models.ContentModel import Content
from .models.CourseModel import Course
from .models.SubscriptionModel import Subscription
from django.http import HttpResponse


def home(request):
	return render(request,'login.html')



def login(request):
	if request.method == 'POST':
		uname=request.POST['uname']
		password=request.POST['paswd']
		finduser=Users.objects.filter(username=uname)
		course=Course.objects.all()

		if finduser:
			#Set session
			user_id=Users.objects.values_list('id',flat=True).get(username=uname)
			#user_uid=Users.objects.values_list('useruid',flat=True).get(username=uname)
			#Setting session values
			request.session['user']=uname
			request.session['id']=user_id
			userdata=Users.objects.filter(username=uname)
			data={}
			data['data']=userdata
			data['course']=course
			return render(request,'homepage.html',data)
		else:
			return HttpResponse('User not found')

#Show the content that is created by a teacher/admin
def mycontentshow(request,id,uid):





def profiledetails(request,id,uid):
	finduser=Users.objects.filter(id=id)
	return render(request,'myprofile.html',{'userdet':finduser})

def editprofile(request,id,uid):
	finduser=Users.objects.filter(id=id)
	newemail=request.POST['updatedemail']
	for x in finduser:
		x.email=newemail

	x.save()
	return HttpResponse('Data Saved')

#Needs to be workedon
def viewavailablecontents(request):
	if request.session.get('user') is not None:
		userid=request.session.get('id')
		subscribelist=Subscription.objects.filter(userid=userid).values()
		course=Course.objects.all()
		'''
		data={}
		data['c']=Course.objects.all()
		data['status']=subscribelist
		'''
		return render(request,'viewavailablecontents.html',{'c':course})
	else:
		return redirect('/')

def enrollcourse(request,id,uid):
	courseid=Course.objects.values_list('id',flat=True).get(id=id)
	coursename=Course.objects.values_list('coursename',flat=True).get(id=id)
	userid=request.session.get('id')
	username=Users.objects.values_list('username',flat=True).get(id=userid)
	subscription=Subscription.objects.filter(userid=userid)
	subscribe=Subscription(courseid=courseid,userid=userid,coursename=coursename,username=username,isenrolled=True)
	subscribe.save()
	return render(request,'homepage.html')


def profilepicchange(request):
	pic = request.FILES['image']
	uname=request.session.get('user')

	userData=Users.objects.filter(username=uname)
	for x in userData:
		x.image=pic
	
	x.save()
	return render(request,'homepage.html')

def logout(request):
    request.session.flush()
    return redirect('/')

def register(request):
	if request.method == 'POST':
		fname= request.POST['fname']
		lname= request.POST['lname']
		email= request.POST['email']
		uname= request.POST['uname']
		passwd= request.POST['passwd']
		confpas= request.POST['confpas']
		getusertype=request.POST['choice']
		
		if getusertype == 'Teacher':
			setusertype="tch"
		else:
			setusertype="stu"

		if passwd == confpas:
			users=Users()
			users.firstname=fname
			users.lastname=lname
			users.username=uname
			users.email=email
			users.password=passwd
			users.usertype=setusertype
			users.save()
			return HttpResponse('Data Saved')
		
	elif request.method == 'GET':
		return render(request,'register.html')
		