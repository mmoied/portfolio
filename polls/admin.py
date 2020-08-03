from django.contrib import admin

# Register your models here.
from .models import work,project,skills

admin.site.register(work)
admin.site.register(project)
admin.site.register(skills)