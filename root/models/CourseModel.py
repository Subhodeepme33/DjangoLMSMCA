from django.db import models
import uuid

class Course(models.Model):
	courseuid=models.UUIDField(default=uuid.uuid4, editable=False)
	coursename=models.CharField(max_length=50)
	coursecategory=models.CharField(max_length=50,blank=True)

	class Meta:
		db_table="course"

	def __str__(self):
		return str(self.courseuid)