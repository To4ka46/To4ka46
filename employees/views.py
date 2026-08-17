from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import EmployeeProfile, EmployeeImage
from .forms import SingleImageUploadForm

@login_required
def add_employee_image(request, pk):
    employee = get_object_or_404(EmployeeProfile, pk=pk)
    existing_max = employee.images.aggregate(models.Max('order'))['order__max'] or 0
    next_order = existing_max + 1

    if request.method == 'POST':
        form = SingleImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_obj = form.save(commit=False)
            image_obj.employee = employee
            if not image_obj.order:
                image_obj.order = next_order
            image_obj.save()
            return redirect('employee_detail', pk=employee.pk)
    else:
        form = SingleImageUploadForm(initial={'order': next_order})

    return render(request, 'add_single_image.html', {
        'employee': employee,
        'form': form,
        'next_order': next_order,
    })

def employee_list(request):
    employees = EmployeeProfile.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(EmployeeProfile, pk=pk)
    images = employee.images.all().order_by('order')
    
    return render(request, 'employee_detail.html', {
        'employee': employee,
        'images': images,
    })

def home(request):
    employees = EmployeeProfile.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})