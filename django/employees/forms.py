from users.models import User

import django.forms as forms


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=20)
    number_id = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)
    group = forms.ChoiceField(choices=[
        ('admin', 'Admin'),
        ('user', 'User'),
    ])

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email
