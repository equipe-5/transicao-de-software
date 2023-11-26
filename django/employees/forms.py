from employees.models import Employee
from users.models import User

import django.forms as forms
from django.core.validators import MinLengthValidator


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=20, validators=[
        MinLengthValidator(14)])
    number_id = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)
    group = forms.ChoiceField(choices=[
        ('admin', 'Admin'),
        ('user', 'Usuário'),
    ])

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email

    def clean_number_id(self):
        number_id = self.cleaned_data['number_id']
        if Employee.objects.filter(number_id=number_id).exists():
            raise forms.ValidationError('Crachá já cadastrado')
        return number_id
