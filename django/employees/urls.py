from employees.views import (EmployeeCreateView, EmployeeDeleteView,
                             EmployeeListView)

from django.urls import path

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('<uuid:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),
]
