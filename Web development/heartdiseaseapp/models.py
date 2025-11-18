from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class heartModel(models.Model):

    age=models.FloatField()
    sex=models.FloatField()
    cp=models.FloatField()
    chol=models.FloatField()
    thalach=models.FloatField()
    exang=models.FloatField()
    oldpeak=models.FloatField()
    ca=models.FloatField()
