from django.db import models

class Review(models.Model):
	
	comment=models.CharField(max_length=150)
	username=models.CharField(max_length=50)
	#star=models.IntegerField(default=0)
	courseuid=models.CharField(max_length=100)

	class Meta:
		db_table="review"