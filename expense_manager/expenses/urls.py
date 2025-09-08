from django.urls import path
from .views import ExpenseListCreateView, ExpenseRetrieveUpdateDeleteView

urlpatterns = [
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:id>/', ExpenseRetrieveUpdateDeleteView.as_view(), name='expense-detail-update-delete'),
]
