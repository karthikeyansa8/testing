from .views import Form
from django.urls import path,include

urlpatterns = [
    path('form/',Form.as_view(),name='form')
]
