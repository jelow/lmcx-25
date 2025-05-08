from django.views.generic import DetailView
from events.models import Events

class EventDetailView(DetailView):
    model = Events
    template_name = "events/events_detail.html"
    httpmethods = ["GET"]
    queryset = Events.objects.all()
