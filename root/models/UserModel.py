from django.db import models
import uuid

class Users(models.Model):
	#default ID
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	username=models.CharField(max_length=50)
	email=models.EmailField()
	password=models.CharField(max_length=100)
	useruid=models.UUIDField(default=uuid.uuid4, editable=False)
	usertype=models.CharField(max_length=5)
	image=models.ImageField(upload_to='uploads/profilepics',blank=True)
	useractive=models.IntegerField(default=1)

	class Meta:
		db_table="users"

	'''
	def __str__(self):
		return str(self.useruid)
	'''