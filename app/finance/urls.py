from django.urls import path
from . import views

urlpatterns = [
    path("client_list/", views.client_list, name="client_list"),
    path("transactions_list/",views.transactions_list, name="transactions_list"),
]