from rest_framework import generics
from .models import Expense
from .serializers import ExpenseSerializer


# Create your views here.
class ExpenseCreateView(generics.CreateAPIView):
    """
    POST API endpoint that creates a new Expense record in the database.

    The request body should have the following format (JSON):
        {
            "title": "string",        # Title of the expense
            "amount": float,          # Amount of the expense
            "date": "YYYY-MM-DD",     # Date of the expense
            "description": "string"   # (Optional) Additional details
        }

    Responses:
        201 Created: Returns the created expense as JSON.
        400 Bad Request: Returned if validation fails.
        405 Method Not Allowed: Returned if the request is not POST.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
