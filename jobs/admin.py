from django.contrib import admin
from .models import Job
class JobAdmin(admin.ModelAdmin):
	# fields = ('title','description','location','type','category','last_date','company_name','company_description','website','created_at','filled','salary','required_exp')
	list_display = ('title','description','location','jtype','category','post_image','last_date','company_name','company_description','website','created_at','status','posts','required_exp')

admin.site.register(Job,JobAdmin)
# Register your models here.
