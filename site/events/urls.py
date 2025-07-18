from django.urls import path
from .views.list_view import EventListView
from .views.detail_view import EventDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', EventListView.as_view(), name='events_list'),
    path('list/<str:type>/', EventListView.as_view(), name='events_list_by_type'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
