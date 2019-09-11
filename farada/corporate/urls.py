from django.urls import path
from .views import home_page,about_page,contact_page

app_name='corporate'
urlpatterns = [
    path('', home_page, name='home'),
    path('about-us', about_page, name='about'),
    path('contact-us', contact_page, name='contact'),
]