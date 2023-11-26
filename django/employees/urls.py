from employees.views import EmployeeCreateView, EmployeeListView

from django.urls import path

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('create/', EmployeeCreateView.as_view(), name='employee-create'),
]
