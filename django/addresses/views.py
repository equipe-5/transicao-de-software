from addresses.forms import AddressForm
from addresses.models import Address
from employees.models import Employee
from users.models import User

from django.db.transaction import atomic
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView


class AdressCreateView(FormView):
    model = Address
    template_name = 'address_form.html'
    form_class = AddressForm
    success_url = reverse_lazy('employee-list')

    def get(self, request, *args, **kwargs):
        user_form = request.session.get('user_form')
        if not user_form:
            return redirect('employee-create')

        form = AddressForm()
        return render(request, self.template_name, {'form': form})

    def create_user(self, address):
        user_form = self.request.session.get('user_form')

        user = User.objects.create_user(
            username=user_form['email'],
            email=user_form['email'],
            password=user_form['password'],
        )

        if user_form['group'] == 'admin':
            user.is_staff = True

        employee = Employee.objects.create(
            user=user,
            name=user_form['name'],
            phone=user_form['phone'],
            number_id=user_form['number_id'],
            role=user_form['role'],
            address=address
        )

        employee.save()

    @atomic
    def post(self, request, *args, **kwargs):
        form = AddressForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data

            address = Address.objects.create(
                street=form['street'],
                number=form['number'],
                neighborhood=form['neighborhood'],
                city=form['city'],
                state=form['state'],
                zipcode=form['zipcode'],
            )

            if self.request.session.get('user_form'):
                self.create_user(address)
                self.request.session.pop('user_form')

            return super().form_valid(form)

        return render(request, self.template_name, {'form': form})
