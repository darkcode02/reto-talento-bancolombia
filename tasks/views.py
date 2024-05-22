from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Guion
from .forms import GuionForm

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('guiones')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

@login_required
def guiones(request):
    guiones = Guion.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'guiones.html', {"guiones": guiones})


@login_required
def create_guion(request):
    if request.method == "GET":
        return render(request, 'create_guion.html', {"form": GuionForm})
    else:
        try:
            form = GuionForm(request.POST)
            new_guion = form.save(commit=False)
            new_guion.user = request.user
            new_guion.save()
            return redirect('guiones')
        except ValueError:
            return render(request, 'create_guion.html', {"form": GuionForm, "error": "Error creating guion."})

def home(request):
    return render(request, 'home.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('guiones')

@login_required
def guion_detail(request, guion_id):
    if request.method == 'GET':
        guion = get_object_or_404(Guion, pk=guion_id, user=request.user)
        form = GuionForm(instance=guion)
        return render(request, 'guion_detail.html', {'guion': guion, 'form': form})
    else:
        try:
            guion = get_object_or_404(Guion, pk=guion_id, user=request.user)
            form = GuionForm(request.POST, instance=guion)
            form.save()
            return redirect('guiones')
        except ValueError:
            return render(request, 'guion_detail.html', {'guion': guion, 'form': form, 'error': 'Error updating guion.'})

@login_required
def complete_guion(request, guion_id):
    guion = get_object_or_404(Guion, pk=guion_id, user=request.user)
    if request.method == 'POST':
        guion.datecompleted = timezone.now()
        guion.save()
        return redirect('guiones')


@login_required
def delete_guion(request, guion_id):
    guion = get_object_or_404(Guion, pk=guion_id, user=request.user)
    if request.method == 'POST':
        guion.delete()
        return redirect('guiones')
    
