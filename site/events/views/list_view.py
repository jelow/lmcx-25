from datetime import date

from django.db.models import QuerySet
from django.views.generic import ListView
from events.models import Events


class EventListView(ListView):
    model = Events
    paginate_by = 10
    context_object_name = "events_list"
    event_list: str = None
    today: date = None

    def __init__(self, **kwargs):
        self.event_list = kwargs.get("event_list", None)
        self.template = kwargs.get("template_name", "events/events_list.html")
        super().__init__(**kwargs)

    def get_queryset(self) -> QuerySet[Events]:
        self.event_list = self.kwargs.get("list", None)
        self.today = date.today()
        if self.event_list == "Home":
            # Home page: show all upcoming events
            return self.model.objects.filter(date__gte=self.today).order_by("date")
        else:
            # Events page: show all non-archived events (even past ones)
            return self.model.objects.filter(archived=False).order_by("date")

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["events_list"] = self.get_queryset()
        context["current_url"] = self.request.get_full_path()
        return context
