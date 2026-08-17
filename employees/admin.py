from django.contrib import admin
from .models import EmployeeProfile, Skill,  EmployeeSkill, EmployeeImage

class EmployeeImageInline(admin.TabularInline):
    model = EmployeeImage
    extra = 1  
    fields = ('image', 'order')

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    inlines = [EmployeeImageInline]
    list_display = ('first_name', 'last_name', 'middle_name')
    search_fields = ('first_name', 'last_name')


class EmployeeSkillInline(admin.TabularInline):
    model = EmployeeSkill
    extra = 1
    fields = ('skill', 'level')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
