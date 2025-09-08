from django.urls import path
from .views import ExpenseCreateView

urlpatterns = [
    path('expenses/', ExpenseCreateView.as_view(), name='expense-create'),
]
