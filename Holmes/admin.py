from django.contrib import admin
from .models import User,Jobs,Degree,Skill
class JobsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'last_date',
    )

admin.site.register(User)
admin.site.register(Jobs,JobsAdmin)
admin.site.register(Degree)
admin.site.register(Skill)
# Register your models here.
