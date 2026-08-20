from .models import Employee

def company_stats(request):
    return {
        'total_employees': Employee.objects.count(),
    }
