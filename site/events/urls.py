from django.urls import path
from .views.list_view import EventListView
from .views.detail_view import EventDetailView

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), {'list': 'Home'}, name='home'),
    path('list/', EventListView.as_view(), {'list': 'All'}, name='list'),
    path('<int:pk>/', EventDetailView.as_view(), name='detail'),
]
