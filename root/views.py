from django.shortcuts import render,redirect
from .models.UserModel import Users
from .models.ContentModel import Content
from .models.CourseModel import Course
from .models.SubscriptionModel import Subscription
from .models.Review import Review
from .models.CategoryModel import Category
from django.http import HttpResponse
from django.http import JsonResponse
 
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
		for x in finduser:
			status=x.useractive
	
		if finduser and status == 1:			
			user_id=Users.objects.values_list('id',flat=True).get(username=uname)
			request.session['user']=uname
			request.session['id']=user_id
			userdata=Users.objects.filter(username=uname)
			data={}
			data['data']=userdata
			data['course']=course			
			return render(request,'homepage.html',data)

		elif finduser and status == 0:
			err="Your account is suspended. Contact Adminstrator"
			return render(request,'login.html',{'err':err})
		
		else:
			return HttpResponse('<script>alert("User not found")</script>')

	
	elif request.method == 'GET':
		if 'user' in request.session and 'id' in request.session:
			uname=request.session.get('user')
			course=Course.objects.all()
			userdata=Users.objects.filter(username=uname)
			data={}
			data['data']=userdata
			data['course']=course
			return render(request,'homepage.html',data)
	

def showenrollments(request):
	if request.method == 'GET':
		userid=request.session.get('id')
		enrolledcourses=Subscription.objects.filter(userid=userid)
		return render(request,'enrollment.html',{'enrolled':enrolledcourses})


def ratings(request):
	category=Category.objects.all()
	data={}
	data['category']=category
	return render(request,'ratings.html',data)

def showchart(request):
	category=request.POST['cat']
	getcourse=Course.objects.filter(coursecategory=category)	
	labels=[]
	data=[]
	for x in getcourse:
		cname=x.coursename
		getcoursecuid=Course.objects.values_list('courseuid',flat=True).get(coursename=cname)
		cuid=str(getcoursecuid)
		totalcomments=Review.objects.filter(courseuid=cuid).count()
		graphdata.add(cname,totalcomments)
	

	items = graphdata.items() 
	for item in items:
		labels.append(item[0]),data.append(item[1])
	
	graphdata.clear()
	return render(request,'graph.html',{
		'labels':labels,
		'data':data,
		})	


class my_dictionary(dict): 
  
    def __init__(self): 
        self = dict() 
          
    def add(self, key, value): 
        self[key] = value 
  

graphdata = my_dictionary() 
  



def mycontentshow(request,id,uid):
	useractiveid=request.session.get('id') #3
	useractivename=request.session.get('user') #nkar
	coursescreated=Course.objects.filter(createdby=useractivename)
	return render(request,'mycreations.html',{'data':coursescreated})




def profiledetails(request,id,uid):
	user=Users.objects.filter(id=id)
	return render(request,'myprofile.html',{'userdet':user})


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
	response=False
	for x in subscription:
		if courseid == x.courseid:
			response=True

	if response == True:
		return HttpResponse('<script>alert("You are already enrolled in this course.Choose else.") </script>')
	else:
		subscribe=Subscription(courseid=courseid,userid=userid,coursename=coursename,username=username,isenrolled=True)
		subscribe.save()
		if 'user' in request.session and 'id' in request.session:
			uname=request.session.get('user')
			course=Course.objects.all()
			userdata=Users.objects.filter(username=uname)
			data={}
			data['data']=userdata
			data['course']=course
			return render(request,'homepage.html',data)


def profilepicchange(request):
	pic = request.FILES['profilepic']
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
		err={}
		if passwd == confpas:
			users=Users()

			if fname is None or fname in ['test','abc','hi','hello']:
				err['fname']="Please enter a valid firstname"
			else:
				users.firstname=fname.lower()

			if lname is None or lname in ['test','abc','hi','hello']:
				err['lname']="Please enter a valid Lastname"
			else:
				users.lastname=lname.lower()

			if uname is None:
				err['uname']="Enter a valid username "
			else:
				users.username=uname.lower()
			if email is None:
				err['email']="Enter a valid email "
			else:
				users.email=email.lower()	
			if len(passwd) < 8:	
				err['pass']="Length of password must be 8 characters"
			else:
				users.password=passwd.lower()
			users.usertype=setusertype.lower()
		
		if not err:	
			users.save()
			return HttpResponse('True')
		else:
			print(err)
			return render(request,'register.html',{'err':err})
		
	elif request.method == 'GET':
		return render(request,'register.html')


def deletecontent(request,id):

	getcourse=Course.objects.filter(id=id)
	getcourseuid=Course.objects.values_list('courseuid',flat=True).get(id=id)
	fetchallcontentforthecourse=Content.objects.filter(cuid=getcourseuid)
	fetchallcontentforthecourse.delete()
	getcourse.delete()
	return HttpResponse('<script>alert("Content is deleted"); window.history.back(); location.reload(true);  </script>')



def logout(request):
    request.session.flush()
    return redirect('/')
