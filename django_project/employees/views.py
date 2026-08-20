from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Employee

def home(request):
    # 4 последних по дате приёма
    recent_employees = Employee.objects.all()[:4]
    
    return render(request, 'employees/home.html', {'recent_employees': recent_employees})

def employee_list(request):
    employees = Employee.objects.all().order_by('-hire_date')
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Тоже ничего не присваиваем
    return render(request, 'employees/employee_list.html', {'page_obj': page_obj})

def employee_detail(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    images = list(emp.images.all())
    emp.main_image = images[0].image if images else None
    emp.gallery_images = images[1:]  # без первого
    emp.skills_with_levels = emp.employeeskill_set.select_related('skill').all()
    return render(request, 'employees/employee_detail.html', {'employee': emp})
