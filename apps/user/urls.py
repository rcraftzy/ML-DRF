from django.urls import path
from .views import *

urlpatterns = [
    path('create', CreateUserProfileView.as_view()),
    path('profile/<account>', DetailUserProfile.as_view())
]
