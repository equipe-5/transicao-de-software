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

    street = forms.CharField(max_length=100)
    number = forms.CharField(max_length=5)
    neighborhood = forms.CharField(max_length=50)
    city = forms.CharField(max_length=25)
    state = forms.ChoiceField(
        choices=[
            ('AC', 'AC'),
            ('AL', 'AL'),
            ('AP', 'AP'),
            ('AM', 'AM'),
            ('BA', 'BA'),
            ('CE', 'CE'),
            ('DF', 'DF'),
            ('ES', 'ES'),
            ('GO', 'GO'),
            ('MA', 'MA'),
            ('MT', 'MT'),
            ('MS', 'MS'),
            ('MG', 'MG'),
            ('PA', 'PA'),
            ('PB', 'PB'),
            ('PR', 'PR'),
            ('PE', 'PE'),
            ('PI', 'PI'),
            ('RJ', 'RJ'),
            ('RN', 'RN'),
            ('RS', 'RS'),
            ('RO', 'RO'),
            ('RR', 'RR'),
            ('SC', 'SC'),
            ('SP', 'SP'),
            ('SE', 'SE'),
            ('TO', 'TO'),
        ]
    )
    zipcode = forms.CharField(max_length=10, min_length=10)

    class Meta:
        model = Employee
        fields = ['name', 'phone', 'number_id',
                  'role', 'group', 'email', 'password', 'street',
                  'number', 'neighborhood', 'city', 'state', 'zipcode']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email já cadastrado')
        return email
