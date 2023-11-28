from addresses.models import Address
from employees.forms import EmployeeForm
from employees.models import Employee
from users.models import User

from django.db.transaction import atomic
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView
from django.views.generic.edit import FormView


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'


class EmployeeCreateView(FormView):
    model = Employee
    template_name = 'employee_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee-list')

    def create_user_form(self, form) -> User:
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        group = form.cleaned_data['group']

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        if group == 'admin':
            user.is_staff = True

        user.save()

        return user

    def create_address_form(self, form) -> Address:
        street = form.cleaned_data['street']
        number = form.cleaned_data['number']
        city = form.cleaned_data['city']
        state = form.cleaned_data['state']
        zipcode = form.cleaned_data['zipcode']

        address = Address(
            street=street,
            number=number,
            city=city,
            state=state,
            zipcode=zipcode
        )

        address.save()

        return address

    def create_employee_form(self, form, user: User, address: Address):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        number_id = form.cleaned_data['number_id']
        role = form.cleaned_data['role']

        employee = Employee(
            user=user,
            address=address,
            name=name,
            phone=phone,
            number_id=number_id,
            role=role
        )

        employee.save()

    @atomic
    def form_valid(self, form):
        user = self.create_user_form(form)
        address = self.create_address_form(form)
        self.create_employee_form(form, user, address)
        return super().form_valid(form)


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employee-list')

    def update_user(self, form, user_instance: User) -> User:
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        group = form.cleaned_data['group']

        user_instance.username = email
        user_instance.password = password
        user_instance.email = email

        if group == 'admin':
            user_instance.is_staff = True

        user_instance.save()
        return user_instance

    def update_address(self, form, address_instance: Address) -> Address:
        street = form.cleaned_data['street']
        number = form.cleaned_data['number']
        city = form.cleaned_data['city']
        state = form.cleaned_data['state']

        address_instance.street = street
        address_instance.number = number
        address_instance.city = city
        address_instance.state = state

        address_instance.save()
        return address_instance

    @atomic
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        employee_instance = Employee.objects.get(id=self.kwargs['pk'])
        address_instance = self.update_address(form, employee_instance.address)
        user_instance = self.update_user(form, employee_instance.user)

        employee_instance.address = address_instance
        employee_instance.user = user_instance
        employee_instance.name = form.cleaned_data['name']
        employee_instance.phone = form.cleaned_data['phone']
        employee_instance.number_id = form.cleaned_data['number_id']
        employee_instance.role = form.cleaned_data['role']
        employee_instance.save()

        return super().form_valid(form)


class EmployeeDeleteView(DeleteView):
    """Product Delete View."""
    model = Employee
    template_name = 'employee_confirm_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee-list')
