from django.db import models


# Create your models here.
class MtaInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    card = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    callTime = models.CharField(max_length=255)
    policyNumber = models.CharField(max_length=255)
    reportNumber = models.CharField(max_length=255)
    principalDate = models.CharField(max_length=255)
    kindInsurance = models.CharField(max_length=255)
    dateInsurance = models.CharField(max_length=255)
    caseDesc = models.CharField(max_length=1000)
    workMedicare = models.CharField(max_length=1000)
    bodyHealth = models.CharField(max_length=255)
    outpatient = models.CharField(max_length=1000)
    hospital = models.CharField(max_length=1000)


