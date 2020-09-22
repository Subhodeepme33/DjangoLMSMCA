from django.contrib import admin
from .models.UserModel import Users
from .models.CourseModel import Course
from .models.ContentModel import Content
from .models.SubscriptionModel import Subscription
from .models.CategoryModel import Category
from embed_video.admin import AdminVideoMixin


class UsersAdmin(admin.ModelAdmin):
	list_display=['firstname','lastname','username','email','useruid']

	def __str__(self):
		return str(self.useruid)

class CourseAdmin(admin.ModelAdmin):
	list_display=['courseuid','coursename']

	def __str__(self):
		return str(self.courseuid)

class ContentAdmin(AdminVideoMixin,admin.ModelAdmin):
	list_display=['contentheading']

	def __str__(self):
		return str(self.cuid)

class SubscriptionAdmin(admin.ModelAdmin):
	list_display =[ 'coursename' , 'username']
	
	def __str__(self):
		return str(self.courseid)



admin.site.register(Users,UsersAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Subscription,SubscriptionAdmin)
admin.site.register(Category)

