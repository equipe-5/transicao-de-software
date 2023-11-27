from addresses.models import Address

from django.forms import ModelForm


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = [
            'street',
            'number',
            'neighborhood',
            'city',
            'state',
            'zipcode',
        ]
