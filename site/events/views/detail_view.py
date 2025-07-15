from django.views.generic import DetailView
from events.models import Events

class EventDetailView(DetailView):
    model = Events
    template_name = "events/events_detail.html"
    httpmethods = ["GET"]
    queryset = Events.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["return_url"] = self.request.GET.get('return_to', '')
        return context