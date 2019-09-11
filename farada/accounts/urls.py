from django.urls import path
from .views import (
    select_registration, 
    participant_registration,
    provider_registration, 
    login_page,
    login,
    redirect_to_dashboard,
    admin_error_page,
)

app_name='accounts'
urlpatterns = [
    path('choose-registration/', select_registration, name='select_reg'),
    path('provider-registration/', provider_registration, name='provider_reg'),
    path('participant-registration/', participant_registration, name='participant_reg'),
    path('redire-to-dashboard/', redirect_to_dashboard, name='redirect'),
    path('login/',login_page, name='login-page'),
    path('login-url/',login, name='login'),
    path('admin-error-page/',admin_error_page, name='admin_error'),
]