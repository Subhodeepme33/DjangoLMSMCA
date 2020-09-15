from django.db import models
from datetime import datetime
import uuid

class Course(models.Model):
	courseuid=models.UUIDField(default=uuid.uuid4, editable=False)
	coursename=models.CharField(max_length=50)
	coursecategory=models.CharField(max_length=50,blank=True)
	createdby=models.CharField(max_length=50,default=0)
	courseimages=models.ImageField(upload_to='uploads/coursepics',blank=True)
	createdat=models.DateTimeField(default=datetime.now()) 

	class Meta:
		db_table="course"

	def __str__(self):
		return str(self.courseuid)