from django.db import models

class Analysis(models.Model):
    user_name=models.CharField("Name", max_length=70)
    report = models.TextField("Report")
    age = models.IntegerField("Age")
    date = models.DateTimeField("Publish date")

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name= 'Analys'
        verbose_name_plural = 'Analysis'


