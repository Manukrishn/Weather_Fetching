from django.db import models

# Create your models here.

class Weather_check(models.Model):
    Location = models.CharField(max_length=50, default=None, null=True)
    main = models.CharField(max_length=50, default=None, null=True)
    icon = models.FileField(upload_to='static/icons', default=None, null=True)
    temperature = models.FloatField(default=None, null=True)
    

    def __str__(self):
        return f"{self.Location} - {self.temperature}°C"
