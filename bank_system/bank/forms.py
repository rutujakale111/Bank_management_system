from django import forms
from .models import Customer, Account, Transaction

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['customer', 'account_number', 'account_type', 'balance']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'type', 'amount']
