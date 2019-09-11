from django.urls import path
from .views import (
    provider_dashboard,
    participant_dashboard,
    provider_list,
    participants_list,
    )

app_name='user_dashboard'
urlpatterns = [
    path('participant',participant_dashboard, name='participant'),
    path('provider',provider_dashboard, name='provider'),
    path('providers',provider_list, name='providers'),
    path('participants',participants_list, name='participants'),
]