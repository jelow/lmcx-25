from announcements.models import Announcement
from django.views.generic import DetailView


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = "announcements/announcements_detail.html"
    httpmethods = ["GET"]
    queryset = Announcement.objects.all()
