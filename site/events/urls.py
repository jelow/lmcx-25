from django.urls import path
from .views.list_view import EventListView
from .views.detail_view import EventDetailView

urlpatterns = [
    path('', EventListView.as_view(), name='events_list'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
]
