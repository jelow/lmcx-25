from django.urls import path
from .views.list_view import EventListView
from .views.detail_view import EventDetailView

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), name='list'),
    path('list/<str:type>/', EventListView.as_view(), name='list_by_type'),
    path('<int:pk>/', EventDetailView.as_view(), name='detail'),
]
