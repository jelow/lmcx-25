from django.db import models

class Events(models.Model):
    EVENT_TYPES = [
        ("WNCXP", "WNCXP - Wednesday Night Cyclocross Practice"),
        ("Women+Clinic", "Women+ (FWTNB) Clinic"),
        ("LMCX", "Lower Mainland Cyclocross Race"),
        ("KinderCross", "KinderCross - Kids Cyclocross"),
    ]
    title = models.CharField(max_length=50)
    website = models.URLField(max_length=200, blank=True)
    registration_link = models.URLField(max_length=200, blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=EVENT_TYPES, default="LMCX")
    main_image = models.ImageField(upload_to='events/', blank=True, null=True)
    sec_image = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.title + " - " + str(self.date.year)
    