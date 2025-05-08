from django.views.generic import DetailView
from announcements.models import Announcement

class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = "announcements/announcements_detail.html"
    httpmethods = ["GET"]
    queryset = Announcement.objects.all()
