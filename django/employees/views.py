from addresses.models import Address
from employees.forms import EmployeeForm
from employees.models import Employee
from users.models import User

from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
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

        address = Address(
            street=street,
            number=number,
            city=city,
            state=state
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

    def form_valid(self, form):
        user = self.create_user_form(form)
        address = self.create_address_form(form)
        self.create_employee_form(form, user, address)
        return super().form_valid(form)


class EmployeeDeleteView(DeleteView):
    """Product Delete View."""
    model = Employee
    template_name = 'employee_confirm_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee-list')
