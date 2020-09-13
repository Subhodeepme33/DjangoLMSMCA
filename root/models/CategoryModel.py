from django.db import models

class Category(models.Model):
	category=models.CharField(max_length=100)
		
	class Meta:
		db_table="category"

	def __str__(self):
		return str(self.category)