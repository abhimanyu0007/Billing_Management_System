from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .forms import BillForm,CustomerContactForm



# Create your views here.
@login_required(login_url='loginPage')
def home(request):
    products = Product.objects.all()
    Total_Products = Product.objects.all().count()
    Total_Customers = Customer.objects.all().count()
    Total_Bills = Bill.objects.all().count()
    bill = Bill.objects.all()
    

    context = {'bill': bill, 'products': products, 'Total_Products': Total_Products,
               'Total_Customers': Total_Customers, 'Total_Bills': Total_Bills}

    return render(request, 'bill/home.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            password1 = "*" * len(password)
            Login.objects.create(username=username, password=password1)
            return redirect('/')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'bill/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url='loginPage')
def products(request):
    products = Product.objects.all()
    product_name = request.POST.get('product_name')
    price = request.POST.get('price')
    if request.method == "POST":
        Product.objects.create(Product_Name=product_name, Price=price)

    return render(request, 'bill/products.html', {'products': products})


@login_required(login_url='loginPage')
def customers(request):
    customers = Customer.objects.all()
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    address = request.POST.get('address')
    birthdate = request.POST.get('dob')
    if request.method == "POST":
        Customer.objects.create(
            first_name=first_name, last_name=last_name, address=address, dob=birthdate)
    return render(request, 'bill/customers.html', {'customers': customers})


@login_required(login_url='loginPage')
def billing(request):
    Bills = Bill.objects.all()
    form = BillForm()
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            form = BillForm()
   
    return render(request, 'bill/billing.html', {'Bills': Bills, 'form': form})


@login_required(login_url='loginPage')
def receipt(request, pk):
    bill = Bill.objects.get(id=pk)
    context = {'bill': bill}
    return render(request, 'bill/receipt.html', context)

@login_required(login_url='loginPage')
def contacts(request):
    customerContact=CustomerContact.objects.all()
    userContact=UserContact.objects.all()
    formCustomer=CustomerContactForm()
    if request.method == 'POST':
        formCustomer= CustomerContactForm(request.POST)
        if formCustomer.is_valid():
            formCustomer.save()
            formCustomer=CustomerContactForm()

    context={'userContact':userContact,'customerContact':customerContact,'formCustomer':formCustomer}
    return render(request, 'bill/contacts.html',context)
