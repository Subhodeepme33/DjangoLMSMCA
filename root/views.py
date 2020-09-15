from django.shortcuts import render,redirect
from .models.UserModel import Users
from .models.ContentModel import Content
from .models.CourseModel import Course
from .models.SubscriptionModel import Subscription
from django.http import HttpResponse

 
def home(request):
	return render(request,'login.html')



def userhome(request):
	if request.method == 'POST':
		uname=request.POST['uname']
		password=request.POST['paswd']
		finduser=Users.objects.filter(username=uname)
		course=Course.objects.all()
		userid=request.session.get('id')
		enrolledcourses=Subscription.objects.filter(userid=userid)
		if finduser:
			
			user_id=Users.objects.values_list('id',flat=True).get(username=uname)
			request.session['user']=uname
			request.session['id']=user_id
			userdata=Users.objects.filter(username=uname)
			data={}
			data['data']=userdata
			data['course']=course
			
			return render(request,'homepage.html',data)
		else:
			return HttpResponse('User not found')

	elif request.method == 'GET':
		return render(request,'homepage.html')


def showenrollments(request):
	#if request.method == 'GET':
	userid=request.session.get('id')
	enrolledcourses=Subscription.objects.filter(userid=userid)
	return render(request,'enrollment.html',{'enrolled':enrolledcourses})






#Show the content that is created by a teacher/admin
def mycontentshow(request,id,uid):
	useractiveid=request.session.get('id') #3
	useractivename=request.session.get('user') #nkar
	coursescreated=Course.objects.filter(createdby=useractivename)
	return render(request,'mycreations.html',{'data':coursescreated})




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
		#enrolledcourses=Subscription.objects.filter(userid=userid)
		data={}
		data['allcourses']=course

		return render(request,'viewavailablecontents.html',data)
	else:
		return redirect('/')

def enrollcourse(request,id,uid):
	courseid=Course.objects.values_list('id',flat=True).get(id=id)
	coursename=Course.objects.values_list('coursename',flat=True).get(id=id)
	userid=request.session.get('id')
	username=Users.objects.values_list('username',flat=True).get(id=userid)
	subscription=Subscription.objects.filter(userid=userid)
	#Condition checking if a user is already enrolled or not. If yes throw an erri
	#Implement the code
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
		

def logout(request):
    request.session.flush()
    return redirect('/')
