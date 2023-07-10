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


# mta排查医院信息
class MtaCheckHospital(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    hospitalName = models.CharField(max_length=255, db_column="hospital_name")
    hospitalAddress = models.CharField(max_length=255, db_column="hospital_address")
    checkDate = models.CharField(max_length=255, db_column="check_date")
    userInfo = models.CharField(max_length=255, db_column="user_info")
    outpatientNumber = models.IntegerField(db_column="outpatient_number")
    hospitalNumber = models.IntegerField(db_column="hospital_number")
    hospitalStayId = models.CharField(max_length=255, db_column="hospital_stay_id")
    outpatientRecord = models.CharField(max_length=1000, db_column="outpatient_record")
    hospitalStayFirst = models.CharField(max_length=255, db_column="hospital_stay_first")
    mainSymptom = models.CharField(max_length=500, db_column="main_symptom")
    medicalHistory = models.CharField(max_length=2000, db_column="medical_history")
    previousHistory = models.CharField(max_length=2000, db_column="previous_history")
    dischargeDiagnosis = models.CharField(max_length=1000, db_column="discharge_diagnosis")
    remark = models.CharField(max_length=255, db_column="remark")
    otherHospitalInfo = models.CharField(max_length=2000, db_column="other_hospital_info")
    type = models.IntegerField(db_column="type")
    checkContent = models.CharField(max_length=2000, db_column="check_content")
    mtaInfoId = models.IntegerField(db_column="mta_info_id")

    class Meta:
        db_table = 'bd_mta_check_hospital'


# 医院基础信息
class Hospital(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=255, db_column='name')
    address = models.CharField(max_length=255, db_column='address')
    level = models.CharField(max_length=255, db_column='level')
    phone = models.CharField(max_length=255, db_column='phone')
    area = models.CharField(max_length=255, db_column='area')

    class Meta:
        db_table = 'bd_hospital'
