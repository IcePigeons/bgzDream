from django import forms

from docHandle.models import MtaCheckHospital


class CheckHospitalForm(forms.ModelForm):
    class Meta:
        model = MtaCheckHospital
        fields = ['id', 'hospitalName', 'hospitalAddress', 'checkDate', 'userInfo', 'outpatientNumber',
                  'hospitalNumber', 'hospitalStayId', 'outpatientRecord', 'hospitalStayFirst', 'mainSymptom',
                  'medicalHistory', 'previousHistory', 'dischargeDiagnosis', 'remark', 'otherHospitalInfo',
                  'type', 'checkContent', 'surveyResultTime', 'surveyResult', 'mtaInfoId']
