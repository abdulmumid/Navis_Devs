from django.contrib import admin
from .models import ContactRequest, Services, About, Tool, Project, Review, Consult, Dizain, Image, Job, JobApplication, Meropriyatie


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'created_at')  

@admin.register(Services)
class PanelAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'category', 'icon')

admin.site.register(About)

admin.site.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = '__all__'

admin.site.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = '__all__'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'position', 'message', 'photo', 'created_at')

@admin.register(Consult)
class ConsultAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'phone', 'text', 'created_at')

@admin.register(Dizain)
class DizainAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'text', 'image')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'level', 'work_type', 'is_active', 'created_at')
    list_filter = ('category', 'level', 'work_type', 'is_active')
    search_fields = ('title', 'description')


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'job', 'applied_at')
    list_filter = ('applied_at',)
    search_fields = ('name', 'email', 'phone', 'linkedin_url')

@admin.register(Meropriyatie)
class MeropriyatieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date','location')
    list_filter = ('date',)
    search_fields = ('title', 'description')