from django.urls import path
from .views import home, addQuotation, cor

urlpatterns = [
    path('', home, name="home"),
    path('addQuotation', addQuotation, name="quotation"),
    path('cor', cor, name="cor"),
]
