from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Account, Transaction
from .forms import CustomerForm, AccountForm, TransactionForm

# Customer Views
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'bank/customer_list.html', {'customers': customers})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to the customer list view after saving
    else:
        form = CustomerForm()

    return render(request, 'bank/customer_form.html', {'form': form})


def customer_form(request, customer_id=None):
    if customer_id:
        customer = get_object_or_404(Customer, pk=customer_id)
    else:
        customer = None

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('bank:customer_list')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'bank/customer_form.html', {'form': form, 'customer': customer})


# Account Views
def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'bank/account_list.html', {'accounts': accounts})


def account_form(request, account_id=None):
    if account_id:
        account = get_object_or_404(Account, pk=account_id)
    else:
        account = None

    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('bank:account_list')
    else:
        form = AccountForm(instance=account)

    return render(request, 'bank/account_form.html', {'form': form, 'account': account})


# Transaction Views
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'bank/transaction_list.html', {'transactions': transactions})


def transaction_form(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank:transaction_list')
    else:
        form = TransactionForm()

    return render(request, 'bank/transaction_form.html', {'form': form})
