from django.shortcuts import render,redirect
from .models.UserModel import Users
from .models.ContentModel import Content
from .models.CourseModel import Course
from django.http import HttpResponse


def home(request):
	return render(request,'login.html')



def login(request):
	if request.method == 'POST':
		uname=request.POST['uname']
		password=request.POST['paswd']
		finduser=Users.objects.filter(username=uname)
		
		if finduser:
			#Set session
			user_id=Users.objects.values_list('id',flat=True).get(username=uname)
			#user_uid=Users.objects.values_list('useruid',flat=True).get(username=uname)
			#Setting session values
			request.session['user']=uname
			request.session['id']=user_id
			#request.session['useruid']=user_uid
			userdata=Users.objects.filter(username=uname)
			#print(userdata)
			return render(request,'homepage.html',{'data':userdata})
		else:
			return HttpResponse('User not found')


def viewavailablecontents(request):
	if request.session.get('user') is not None:
		course=Course.objects.all()
		return render(request,'viewavailablecontents.html',{'c':course})
	else:
		return redirect('/')



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
		