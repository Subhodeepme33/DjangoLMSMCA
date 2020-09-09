from django.shortcuts import render,redirect
from root.models.CourseModel import Course
from root.models.ContentModel import Content
# Create your views here.

def contentcreate(request):
	if request.method == 'POST':
		cname=request.POST['coursename']
		course=Course(coursename=cname)
		course.save()
		getcourseid=Course.objects.values_list('id',flat=True).get(coursename=cname)

		request.session['activecourse']=getcourseid
		request.session['activecoursename']=cname
		return render(request,'continuecreate.html',{'c':course})
		
	elif request.method == 'GET':
		return render(request,'contentcreate.html')

def viewcontinuecreate(request):
	return render(request,'continuecreate.html')



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
		content=Content(contentheading=head,contentbody=cont,contenturl=url,cuid=courseuid)

		content.save()
		return render(request,'continuecreate.html')

	elif request.method == 'GET':
		return render(request,'continuecreate.html')


def displaycontent(request):
	return render(request,'displaycontent.html')

