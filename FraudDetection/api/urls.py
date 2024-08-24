from django.urls import path
from . import views

urlpatterns = [
    path('check-transaction/', views.checkTransaction, name='check_transaction'),
    path('is-fraud/', views.isFraud, name='is_fraud'),
]