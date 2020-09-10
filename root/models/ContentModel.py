from django.db import models
from .CourseModel import Course
from embed_video.fields import EmbedVideoField

class Content(models.Model):

	#courseuid=models.ForeignKey(Course,on_delete=models.CASCADE,default=None) 
	#contentid=models.IntegerField()
	cuid=models.CharField(max_length=100,blank=True)
	contentheading=models.CharField(max_length=100)
	contentbody=models.TextField()
	contenturl=EmbedVideoField()
	createdby=models.CharField(max_length=100,blank=True)
	createdbyid=models.IntegerField(default=0)
	
	class Meta:
		db_table="content"

	def __str__(self):
		return str(self.cuid)