from rest_framework import serializers

from docHandle.models import MtaCheckHospital


# 自定义ValueSerializer类，继承自Serializer类
class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MtaCheckHospital
        fields = '__all__'
        # 'id', 'hospitalName', 'hospitalAddress', 'checkDate', 'userInfo',
        # 'outpatientNumber', 'hospitalNumber', 'hospitalStayId', 'outpatientRecord', 'hospitalStayFirst'
        # , 'mainSymptom', 'medicalHistory', 'dischargeDiagnosis', 'previousHistory', 'remark',
        # 'otherHospitalInfo'
        # , 'checkContent', 'type', 'mtaInfoId']
