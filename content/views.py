from django.shortcuts import render,redirect
from root.models.CourseModel import Course
from root.models.ContentModel import Content
from root.models.CategoryModel import Category
from django.http import HttpResponse




def contentcreate(request):
	if request.method == 'POST':
		cname=request.POST['coursename']
		ccat=request.POST['category']
		createdby=request.session.get('user')
		course=Course(coursename=cname,coursecategory=ccat,createdby=createdby)
		course.save()
		getcourseid=Course.objects.values_list('id',flat=True).get(coursename=cname)
		
		userid=request.session.get('id')
		request.session['activecourse']=getcourseid
		request.session['activecoursename']=cname
		return render(request,'continuecreate.html',{'c':course})
		
	elif request.method == 'GET':
		category=Category.objects.all()
		return render(request,'contentcreate.html',{'cat':category})

def viewcontinuecreate(request):
	return render(request,'continuecreate.html')

def fetchcontent(request,id,uid):
	getcontent=Content.objects.filter(id=id)
	return render(request,'fetchcontent.html',{'c':getcontent})


def showcontent(request,id,uid):
	getpost=Content.objects.filter(cuid=uid)
	return render(request,'displaycontent.html',{'data':getpost})


def continuecreate(request):

	if request.method == 'POST':
		key=request.session.get('activecourse')
		cid=Course.objects.values_list('courseuid',flat=True).get(id=key)
		head=request.POST['heading']
		url=request.POST['url']
		cont=request.POST['content']
		courseuid=str(cid)
		createdby=request.session.get('user')
		createdbyid=request.session.get('id')
		content=Content(contentheading=head,contentbody=cont,contenturl=url,cuid=courseuid,createdby=createdby,createdbyid=createdbyid)

		content.save()
		return render(request,'continuecreate.html')

	elif request.method == 'GET':
		return render(request,'continuecreate.html')


def displaycontent(request):
	return render(request,'displaycontent.html')


def editcontent(request,id):
	#courseid is fetched suppose 61 
	createdby=request.session.get('id')
	#Fetches me coursuid
	fetchcourseidforid=Course.objects.values_list('courseuid',flat=True).get(id=id) 
	fetchcontentforcourseid=Content.objects.filter(cuid=fetchcourseidforid)
	return render(request,'editcontent.html',{'data':fetchcontentforcourseid})


def editfinal(request,id):
	if request.method== 'POST':
		newbody=request.POST['newbody']
		fetchcontentbyid=Content.objects.filter(id=id)
		for x in fetchcontentbyid:
			x.contentbody=newbody
		x.save()
		return render(request,'homepage.html')
	elif request.method == 'GET':
		return render(request,'editcontentcontinue.html')

def editfinish(request,id):
	fetchcontentbyid=Content.objects.filter(id=id)
	return render(request,'editcontentcontinue.html',{'data':fetchcontentbyid})



def addnew(request,id,uid):
	newhead=request.POST['newhead']
	newbody=request.POST['newbody']
	newurl=request.POST['newurl']
	createdby=request.session.get('user')
	createdbyid=request.session.get('id')
	content=Content(contentheading=newhead,contentbody=newbody,contenturl=newurl,cuid=uid,createdby=createdby,createdbyid=createdbyid)
	content.save()
	return HttpResponse('Data Saved Successfully!')