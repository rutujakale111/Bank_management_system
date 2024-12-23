from django.urls import path
from . import views

app_name = 'bank'

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customer/create/', views.customer_create, name='customer_create'),
    path('customer/<int:customer_id>/edit/', views.customer_form, name='customer_update'),  # Adjust as needed
    path('customer/<int:customer_id>/delete/', views.customer_delete, name='customer_delete'),  # Adjust as needed

    # Account URLs
    path('accounts/', views.account_list, name='account_list'),
    path('accounts/add/', views.account_form, name='account_form'),
    path('accounts/edit/<int:account_id>/', views.account_form, name='account_form_edit'),

    # Transaction URLs
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.transaction_form, name='transaction_form'),
]
