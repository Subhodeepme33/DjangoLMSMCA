from django.db import models
from django.utils import timezone
import uuid

class Teacher(models.Model):
	#default ID
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	username=models.CharField(max_length=50)
	email=models.EmailField()
	password=models.CharField(max_length=100)
	teacheruid=models.UUIDField(default=uuid.uuid4, editable=False)
	image=models.ImageField(upload_to='uploads/profilepics',default=timezone.now)

	class Meta:
		db_table="teacher"