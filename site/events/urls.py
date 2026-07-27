from django.urls import path
from django.views.generic import TemplateView
from .views.list_view import EventListView
from .views.detail_view import EventDetailView

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), {'list': 'Home'}, name='home'),
    path('list/', EventListView.as_view(), {'list': 'All'}, name='list'),
    path('<int:pk>/', EventDetailView.as_view(), name='detail'),
    path('schedule/', TemplateView.as_view(template_name='events/events_schedule.html'), name='schedule'),
]
