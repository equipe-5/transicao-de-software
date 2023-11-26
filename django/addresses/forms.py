import django.forms as forms


class AddressForm(forms.Form):
    street = forms.CharField(max_length=100)
    number = forms.CharField(max_length=10, required=False)
    neighborhood = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
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
    zipcode = forms.CharField(max_length=10)
