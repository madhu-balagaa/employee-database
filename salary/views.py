from django.shortcuts import get_object_or_404, render

from salary.models import Employee

def employee_detail(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    context={
        'employee':employee,
    }
    return render(request,'employee_detail.html',context)



