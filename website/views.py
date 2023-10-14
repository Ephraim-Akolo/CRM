from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home(request):
    context = {}
    records = Record.objects.all()
    context['records'] =  records
    context['recordform'] =  AddRecordForm()
    if request.method == 'POST': #lOGIN
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "There was an error logging in!")
        else:
            login(request, user)
            messages.success(request, "You have been logged in!")
    return render(request, 'home.html', context)
        

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')


def signup_user(request):
    if request.method != 'POST': #GET
        return render(request, 'register.html', {'form':SignUpForm()})
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(request, username=username, password=password)
        login(request, user=user)
        messages.success(request, "You have been logged in!")
        return redirect('home')
    messages.success(request, f"INVALID FORM: {form.errors.as_text()}")        
    return render(request, 'register.html', {'form': form})


def update_delete_record(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')
    context = {}
    record = Record.objects.get(pk=pk)
    context['record'] = record
    context['disabled'] = 'disabled'
    return render(request, 'update_delete.html', context)


def update_user_record(request, pk):
    if not request.user. is_authenticated:
        return redirect('home')
    record = Record.objects.get(pk=pk)
    if request.POST:
        record.name = request.POST['name']
        record.age = request.POST['age']
        record.email = request.POST['email']
        record.seen = True if 'seen' in request.POST else False
        record.save()
        messages.success(request, "Record updated successfully!")
        return redirect('home')
    context = {}
    context['record'] = record
    context['disabled'] = ''
    return render(request, 'update_delete.html', context)


def delete_user_record(request, pk):
    if request.user. is_authenticated:
        if request.POST:
            record = Record.objects.get(pk=pk)
            record.delete()
            messages.success(request, "Record deleted successfully!")
    return redirect('home')


def add_user_record(request):
    if request.user.is_authenticated:
        if request.POST:
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record added sucessfully!")
            else:
                messages.error(request, form.errors.as_text())
    return redirect('home')
