from django.db import models

class TODO(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=255)

    def __str__(self):
        return self.item
    