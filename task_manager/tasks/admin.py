from django.contrib import admin

# Register your models here.
from .models import Task, Comment, User 
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_active','is_staff','is_superuser')
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description','due_date','get_members','status')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'user','text','created_at')
admin.site.register(Task,TaskAdmin)
admin.site.register(Comment,CommentAdmin)   
admin.site.register(User,UserAdmin) 