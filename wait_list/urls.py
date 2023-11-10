from django.urls import path
from .views import WaitListCreateAPIView, WaitListView

urlpatterns = [
    path('api/wait-list/create/', WaitListCreateAPIView.as_view(),
         name='wait-list-create'),
    path('api/waitlist/', WaitListView.as_view(), name='waitlist'),
    # Other URL patterns for your API views
]
