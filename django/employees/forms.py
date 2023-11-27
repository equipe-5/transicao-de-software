from employees.models import Employee
from users.models import User

from django import forms
from django.forms import ModelForm


class EmployeeForm(ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    group = forms.ChoiceField(choices=[
        ('admin', 'Admin'),
        ('user', 'Usuário'),
    ])

    class Meta:
        model = Employee
        fields = ['name', 'phone', 'number_id',
                  'role', 'group', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email
