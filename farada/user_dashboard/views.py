from django.shortcuts import render
from django.conf import settings
from accounts.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def participant_dashboard(request):
    template_name ='user_dashboard/participant_dashboard.html'
    return render(request,template_name,{})

@login_required
def provider_dashboard(request):
    template_name ='user_dashboard/provider_dashboard.html'
    return render(request,template_name,{})

def provider_list(request):
    template_name = 'user_dashboard/provider_list.html'
    providers = User.objects.filter(is_provider=True)
    paginator = Paginator(providers,2)
    page = request.GET.get('page')
    provider_list = paginator.get_page(page)
    context = {'data':provider_list}
    print('print providers')
    print(context)
    return render(request,template_name,context)

def participants_list(request):
    template_name = 'user_dashboard/participant_list.html'
    prarticipants = User.objects.filter(is_participant=True)
    paginator = Paginator(prarticipants,2)
    page = request.GET.get('page')
    prarticipants_list = paginator.get_page(page)
    context = {'data':prarticipants_list}
    print('print participants')
    print(context)
    return render(request,template_name,context)