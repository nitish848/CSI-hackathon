from django.db import models

# Create your models here.
class FIR(models.Model):
    FIR_id=models.AutoField
    FIR_content=models.CharField(max_length=1500, default="")


def __str__(self):
    return self.FIR_content