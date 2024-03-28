from django.db import models

# Create your models here.
from django.urls import reverse

class CompanyModel (models.Model):
    company=models.CharField(max_length=30 )
    ename=models.CharField(max_length=30)
    eid=models.IntegerField()
    eemail=models.EmailField()
    ephn=models.BigIntegerField()
    esal=models.FloatField()

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})


