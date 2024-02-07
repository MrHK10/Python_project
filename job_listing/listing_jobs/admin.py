from django.contrib import admin

# Register your models here.

from .models import Role,Employee,Experience,Source,Company,User,JobListing

admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Experience)
admin.site.register(Source)
admin.site.register(Company)
admin.site.register(User)
admin.site.register(JobListing)
