from announcements.models import Announcement
from django.db.models import QuerySet
from django.views.generic import ListView


class AnnouncementListView(ListView):
    template_name = "announcements/announcements_list.html"
    model = Announcement
    paginate_by = 10
    context_object_name = "announcements_list"

    def get_queryset(self) -> QuerySet[Announcement]:
        return self.model.objects.all().order_by("-date_posted")

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["announcements_list"] = self.get_queryset()
        return context
