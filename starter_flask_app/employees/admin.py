from django.contrib import admin
from .models import EmployeeProfile, Skill, EmployeeSkill
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class EmployeeSkillInline(admin.TabularInline):
    model = EmployeeSkill
    extra = 1

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender')
    search_fields = ('first_name', 'last_name')
    inlines = [EmployeeSkillInline]