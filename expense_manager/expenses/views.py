from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .models import Expense
from .serializers import ExpenseSerializer


# Create your views here.
class ExpenseListCreateView(generics.ListCreateAPIView):
    """
    API endpoint that creates a new Expense record or lists all existing records from the database.
    Supports filtering, searching and ordering.

    Methods:
        GET: Returns a list of all Expense records.
        POST: Creates a new Expense record.
            The request body should have the following format (JSON):
                {
                    "title": "string",        # Title of the expense
                    "amount": float,          # Amount of the expense
                    "date": "YYYY-MM-DD",     # Date of the expense
                    "description": "string"   # (Optional) Additional details
                }

    Responses:
        200 OK: Returned on GET with a list of expenses.
        201 Created: Returned on POST when an expense is successfully created.
        400 Bad Request: Returned if validation fails for the POST data.
    """
    queryset = Expense.objects.all().order_by('id')
    serializer_class = ExpenseSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['date', 'title', 'amount']
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'date', 'amount']
    ordering = ['id']

    def get_queryset(self):
        # Only return expenses of the logged-in user
        return Expense.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to new expenses
        serializer.save(user=self.request.user)


class ExpenseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows to:
      - GET: retrieve a single Expense record by its ID
      - PUT: update all fields of an Expense record by its ID
      - PATCH: update partial fields of an Expense record by its ID
      - DELETE: delete an Expense record by its ID

    URL parameters:
        id (int): The primary key of the expense to retrieve.

    Responses:
        200 OK: For successful GET, PUT, PATCH
        204 No Content: For successful DELETE
        400 Bad Request: For invalid input
        404 Not Found: Returned if no expense with the given ID exists.
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
