from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
from django.contrib.auth import authenticate, login
from .form import RegisterForm, EditAccountForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Enrollment


def register(request):
    template_name = 'accounts/register.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, template_name, context)

@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    context = {}
    context['enrollments'] = Enrollment.objects.filter(user=request.user)
    return render(request, template_name, context)

@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}

    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Os dados da sua conta foram alterardos com sucesso')
            return redirect('accounts:dashboard')
    else: 
        form = EditAccountForm(instance=request.user)
    
    context['form'] = form 
    
    return render(request, template_name, context)

@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    
    context['form'] = form 
    
    return render(request, template_name, context)