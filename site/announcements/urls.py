from django.urls import path
from .views.detail_view import AnnouncementDetailView
from .views.list_view import AnnouncementListView

app_name = 'announcements'

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='list'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='detail'),
]