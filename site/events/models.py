from django.db import models
from tinymce.models import HTMLField


class Events(models.Model):
    EVENT_TYPES = [
        ("wncxp", "WNCXP - Wednesday Night Cyclocross Practice"),
        ("clinic", "Women+ (FWTNB) Clinic"),
        ("lmcx_races", "Lower Mainland Cyclocross Race"),
        ("other_races", "Other Races"),
        ("kindercross", "KinderCross - Kids Cyclocross"),
    ]
    title = models.CharField("Event Name", max_length=50)
    website = models.URLField(max_length=200, blank=True)
    registration_link = models.URLField(max_length=200, blank=True)
    date = models.DateTimeField("Event Date")
    location = models.CharField(max_length=200)
    description = HTMLField("Event Description")
    type = models.CharField(
        "Event Type", max_length=50, choices=EVENT_TYPES, default="lmcx_races"
    )
    main_image = models.ImageField(
        "Main Event Image", upload_to="images/events", blank=True, null=True
    )
    sec_image = models.ImageField(
        "Icon Image", upload_to="images/events", blank=True, null=True
    )
    archived = models.BooleanField("Archived", default=False)

    def __str__(self):
        return self.title + " - " + str(self.date.year)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["-date"]
