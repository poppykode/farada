from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ParticipantSignUpForm,ProviderSignUpForm

# Create your views here.
@login_required
def redirect_to_dashboard(request):
    user = request.user
    if user.is_provider:
        messages.success(request, 'successfully logged in.')
        return redirect('user_dashboard:provider')
    elif user.is_participant:
        messages.success(request, 'successfully logged in.')
        return redirect('user_dashboard:participant')
    messages.error(request,'please use admin url to login or contact webmaster.')
    return redirect('accounts:admin_error')

def select_registration(request):
    template_name = 'registration/select_reg.html'
    context ={}
    return render(request, template_name,context)

def provider_registration(request):
    template_name = 'registration/reg_provider.html'
    if request.method =='POST':
        form = ProviderSignUpForm(request.POST)
        if form.is_valid():
            print('before saving')
            form.save()
            print('after saving')
            messages.success(request,'your registration has been successful.') 
            return redirect(reverse('accounts:login-page'))
    else:
        form = ProviderSignUpForm()
        context = {'form': form}
        return render(request,template_name, context)

def participant_registration(request):
    template_name = 'registration/reg_participant.html'
    if request.method =='POST':
        form = ParticipantSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your registration has been successful.') 
            return redirect(reverse('accounts:login-page'))
    else:
        form = ParticipantSignUpForm()
        context = {'form': form}
        return render(request, template_name, context)

def login_page(request):
    template_name='registration/login.html'
    return render(request,template_name)

def login(request):
    template_name='registration/login.html'
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    print('God is in it')
    print(username)
    print(password)
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return  redirect(reverse('accounts:redirect'))  
    else:
        messages.error(request,'Invalid username or password.') 
        return render(request,template_name) 

def admin_error_page(request):
    template_name = 'registration/admin_error_page.html'
    return render(request,template_name,{})

    
