from django.shortcuts import render

# Create your views here.
def home_page(request):
    template_name ='corporate/home.html'
    context = {}
    print('this is what is in the request')
    print(request)
    return render(request,template_name,context)

def about_page(request):
    template_name ='corporate/about-us.html'
    context = {}
    return render(request,template_name,context)

def contact_page(request):
    template_name ='corporate/contact-us.html'
    context = {}
    return render(request,template_name,context)
