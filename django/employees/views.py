from employees.forms import EmployeeForm
from employees.models import Employee

from django.shortcuts import redirect, render
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

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            request.session['user_form'] = form.cleaned_data
            return redirect('address-create')
        return render(request, self.template_name, {'form': form})


class EmployeeDeleteView(DeleteView):
    """Product Delete View."""
    model = Employee
    template_name = 'employee_confirm_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee-list')
