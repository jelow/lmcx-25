from django.db import models

class Events(models.Model):
    EVENT_TYPES = [
        ("wncxp", "WNCXP - Wednesday Night Cyclocross Practice"),
        ("clinic", "Women+ (FWTNB) Clinic"),
        ("races", "Lower Mainland Cyclocross Race"),
        ("kiddiecross", "KiddieCross - Kids Cyclocross"),
    ]
    title = models.CharField(max_length=50)
    website = models.URLField(max_length=200, blank=True)
    registration_link = models.URLField(max_length=200, blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=EVENT_TYPES, default="races")
    main_image = models.ImageField(upload_to='events/', blank=True, null=True)
    sec_image = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.title + " - " + str(self.date.year)
    