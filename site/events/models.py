from django.db import models

class Events(models.Model):
    title = models.CharField(max_length=50)
    website = models.URLField(max_length=200, blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title + " - " + str(self.date.year)
    