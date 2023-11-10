from django.urls import path
from .views import WaitListCreateAPIView

urlpatterns = [
    path('api/wait-list/create/', WaitListCreateAPIView.as_view(),
         name='wait-list-create'),
    # Other URL patterns for your API views
]
