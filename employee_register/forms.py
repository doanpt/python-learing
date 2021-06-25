from django import forms

from employee_register.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'fullname': 'Full Name',
            'emp_code': 'EMP. code',
            'mobile': 'Mobile',
            'position': 'Position'
        }
