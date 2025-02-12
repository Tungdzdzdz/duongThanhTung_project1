# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            Customer.objects.create(id=user.id, username=user.username, email=user.email)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'customer/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'customer/login.html', {'form': form})

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'customer/profile.html', {'user': request.user})