from django.urls import path
from .views.detail_view import AnnouncementDetailView
from .views.list_view import AnnouncementListView

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcements_list'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='announcements_detail'),
]