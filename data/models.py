from django.db import models

class Csv(models.Model):
    file = models.FileField(upload_to='datafiles/', max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.file)

class Temperature(models.Model):
    x = models.CharField(max_length=200)
    y = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)
    csv = models.ForeignKey(Csv, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.x} - {self.y} - {self.temperature}"