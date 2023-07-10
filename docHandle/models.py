from django.db import models


# Create your models here.
class MtaInfo(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=255, db_column='name')
    card = models.CharField(max_length=255, db_column='card')
    sex = models.CharField(max_length=10, db_column='sex')
    address = models.CharField(max_length=255, db_column='address')
    phone = models.CharField(max_length=255, db_column='phone')
    callTime = models.CharField(max_length=255, db_column='call_time')
    policyNumber = models.CharField(max_length=255, db_column='policy_number')
    reportNumber = models.CharField(max_length=255, db_column='report_number')
    principalDate = models.CharField(max_length=255, db_column='principal_date')
    kindInsurance = models.CharField(max_length=255, db_column='kind_insurance')
    dateInsurance = models.CharField(max_length=255, db_column='date_insurance')
    caseDesc = models.CharField(max_length=1000, db_column='case_desc')
    workMedicare = models.CharField(max_length=1000, db_column='work_medicare')
    bodyHealth = models.CharField(max_length=255, db_column='body_health')
    outpatient = models.CharField(max_length=1000, db_column='outpatient')
    hospital = models.CharField(max_length=1000, db_column='hospital')
    lifeTrackInfo = models.CharField(max_length=255, db_column='life_track_info')

    class Meta:
        db_table = 'bd_mta_info'


class MtaCheckHospital(models.Model):
    id = models.AutoField(primary_key=True)
    hospitalName = models.CharField(max_length=255)
    hospitalAddress = models.CharField(max_length=255)
    checkDate = models.CharField(max_length=255)
    userInfo = models.CharField(max_length=255)
    outpatientNumber = models.IntegerField()
    hospitalNumber = models.IntegerField()
    hospitalStayId = models.CharField(max_length=255)
    outpatientRecord = models.CharField(max_length=1000)
    hospitalStayFirst = models.CharField(max_length=255)
    mainSymptom = models.CharField(max_length=500)
    medicalHistory = models.CharField(max_length=2000)
    previousHistory = models.CharField(max_length=2000)
    dischargeDiagnosis = models.CharField(max_length=1000)
    remark = models.CharField(max_length=255)
    otherHospitalInfo = models.CharField(max_length=2000)
    type = models.IntegerField()
    checkContent = models.CharField(max_length=2000)
    surveyResultTime = models.CharField(max_length=255)
    surveyResult = models.CharField(max_length=1000)
    mtaInfoId = models.IntegerField()

    class Meta:
        db_table = 'bd_mta_check_hospital'


class Hospital(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=255, db_column='name')
    address = models.CharField(max_length=255, db_column='address')
    level = models.CharField(max_length=255, db_column='level')
    phone = models.CharField(max_length=255, db_column='phone')
    area = models.CharField(max_length=255, db_column='area')

    class Meta:
        db_table = 'bd_hospital'
