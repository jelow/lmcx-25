from django.views.generic import ListView
from django.db.models import QuerySet
from typing import Dict
from events.models import Events

class EventListView(ListView):
    template_name = "events/events_list.html"
    model = Events
    paginate_by = 10
    context_object_name = "events_list"
    event_type: str = None

    def get_queryset(self) -> QuerySet[Events]:
        self.event_type = self.kwargs['type'] if 'type' in self.kwargs else None
        if self.event_type is None:
            return self.model.objects.all().order_by("date")
        else:
            return self.model.objects.filter(type=self.event_type).order_by("date")
    
    def get_context_data(self, **kwargs) -> Dict:
        context = super().get_context_data(**kwargs)
        context["events_list"] = self.get_queryset()
        return context
