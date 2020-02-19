from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=255)
    information = models.TextField()

    def __str__(self):
        if len(str(self.name)) > 20:
            return str(self.name)[:20] + '...'
        return self.name
