import json

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from app.models import Item, RentItem
from django.views.decorators.csrf import csrf_exempt


def homepage(request: HttpRequest) -> HttpResponse:
    print('render')
    return render(request, 'index.html')


def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', context={"form":form})


def rental(request: HttpRequest, place_num) -> HttpResponse:
    items = Item.objects.filter(place=place_num)
    context = {'allitems':items}
    return render(request, 'rental.html', context)


@csrf_exempt
def rental_item(request: HttpRequest) -> HttpResponse:
    json_object = json.loads(request.body)
    id_item = json_object.get('id_item')
    item = Item.objects.get(id=id_item)
    date = json_object.get('rent_date')
    rent_item = RentItem(item=item, rented_at=date, user=request.user)
    rent_item.save()
    item.rented = True
    item.save()
    return HttpResponse('')


def logout_request(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/login")


def signup_request(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


def my_rentals(request: HttpRequest) -> HttpResponse:
    orders = RentItem.objects.filter(user=request.user)
    context = {'orders': orders}
    return render(request, 'myrentals.html', context)


def return_item(request: HttpRequest, id_order) -> HttpResponse:
    order = RentItem.objects.get(id=id_order)
    order.item.rented = False
    order.delete()
    return redirect("/myrentals")