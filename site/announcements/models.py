from django.db import models
from tinymce.models import HTMLField

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField("Announcement Content")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " - " + str(self.date_posted.year)
