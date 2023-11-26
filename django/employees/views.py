from employees.forms import EmployeeForm
from employees.models import Employee
from users.models import User

from django.db.transaction import atomic
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'


class EmployeeCreateView(FormView):
    model = Employee
    template_name = 'employee_form.html'
    success_url = reverse_lazy('employee-list')
    form_class = EmployeeForm

    @atomic
    def form_valid(self, form: EmployeeForm) -> HttpResponse:
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

        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        number_id = form.cleaned_data['number_id']
        role = form.cleaned_data['role']

        employee = Employee(
            user=user,
            name=name,
            phone=phone,
            number_id=number_id,
            role=role
        )

        employee.save()

        return super().form_valid(form)
