from django .urls import path
from .views import IndexView  # Import the IndexView from views.py

urlpatterns = [
    path('home', IndexView)  # Add the index view for the root URL
    # Add other URL patterns here as needed
    # path('another/', another_view, name='another_view'),
    # path('example/', example_view, name='example_view'),  
    
]
