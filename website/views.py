from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.


def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error Username Or Password')
            return redirect('home')
    context = {'records': records}
    return render(request, 'base/home.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_page(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You Have successfully Register :)')
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/register_page.html', context)


@login_required(login_url='login')
def record_page(request, pk):
    record = Record.objects.get(id=pk)
    return render(request, 'base/record_page.html', {'record': record})


@login_required(login_url='login')
def delete_page(request, pk):
    record = Record.objects.get(id=pk)
    if request.method == 'GET':
        record.delete()
        messages.success(request, 'Record Deleted successfully')
        return redirect('home')


@login_required(login_url='login')
def record_form(request):
    if request.method == 'POST':
        RecordForm = AddRecordForm(request.POST)
        if RecordForm.is_valid():
            RecordForm.save()
            messages.success(request, 'You Added the record successfully...')
            return redirect('home')
    return render(request, 'base/add_record.html', {'RecordForm': AddRecordForm})


@login_required(login_url='login')
def update_record(request, pk):
    page = 'update'
    record = Record.objects.get(id=pk)
    form = AddRecordForm(instance=record)
    if request.method == 'POST':
        form = AddRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You Have updated the Record successfully')
            return redirect('home')
    context = {'RecordForm': form, 'page': page}
    return render(request, 'base/add_record.html', context)
