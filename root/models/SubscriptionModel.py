from django.db import models
from .CourseModel import Course
from .UserModel import Users

class Subscription(models.Model):
	#id PK
	courseuid=models.ForeignKey(Course,on_delete=models.CASCADE,default=None) #FK
	coursename=models.CharField(max_length=50)
	username=models.CharField(max_length=50)
	useruid=models.ForeignKey(Users,on_delete=models.CASCADE,default=None)
	

	class Meta:
		db_table="subscription"
	
	def __str__(self):
		return str(self.courseuid)