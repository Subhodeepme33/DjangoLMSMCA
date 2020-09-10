from django.db import models
from .CourseModel import Course
from .UserModel import Users

class Subscription(models.Model):
	#id PK
	courseid=models.IntegerField(default=None)
	coursename=models.CharField(max_length=50)
	username=models.CharField(max_length=50)
	userid=models.IntegerField(default=None)
	isenrolled=models.BooleanField(default=False)

	class Meta:
		db_table="subscription"
	
	def __str__(self):
		return str(self.courseuid)