"""
URL mappings for the user API.
"""

from .views import CreateUserView, CreateTokenView, ManagerUserView
from django.urls import path


app_name = 'user'
urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token', CreateTokenView.as_view(), name='token'),
    path('me/', ManagerUserView.as_view(), name='me')
]
