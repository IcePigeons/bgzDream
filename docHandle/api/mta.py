import json

from django.http import JsonResponse

from docHandle.common import success_response

from docHandle.models import MtaCheckHospital, MtaInfo
from docHandle.utils import FileUtil


def save_check_hospital(request):
    if request.method == 'POST':
        request.encoding = 'utf-8'
        data = json.loads(request.body)
        for obj in data:
            # print(obj)
            if obj['type'] == 1:
                mch = MtaCheckHospital(hospitalName=obj['hospitalName'], hospitalAddress=obj['hospitalAddress'],
                                       checkDate=obj['checkDate'],
                                       userInfo=obj['userInfo'], outpatientNumber=obj['outpatientNumber'],
                                       hospitalNumber=obj['hospitalNumber'],
                                       hospitalStayId=obj['hospitalStayId'], outpatientRecord=obj['outpatientRecord'],
                                       hospitalStayFirst=obj['hospitalStayFirst'],
                                       mainSymptom=obj['mainSymptom'], medicalHistory=obj['medicalHistory'],
                                       dischargeDiagnosis= obj['dischargeDiagnosis'],previousHistory=obj['previousHistory'],
                                       remark=obj['remark'], otherHospitalInfo=obj['otherHospitalInfo'],
                                       type=obj['type'])
                mch.save()
            else:
                mch = MtaCheckHospital(hospitalName=obj['hospitalName'], hospitalAddress=obj['hospitalAddress'],
                                       checkDate=obj['checkDate'],
                                       userInfo=obj['userInfo'], remark=obj['remark'], checkContent=obj['checkContent'],
                                       type=obj['type'])
                mch.save()
    return success_response(None)


def download_mta(request):
    if request.method == "GET":
        card = request.GET.get("card")
        mta_info = MtaInfo.objects.filter(card=card).first()
        mta_check_hospital_arr = MtaCheckHospital.objects.filter(mtaInfoId=mta_info.id).filter(type=1)
        un_mta_check_hospital_arr = MtaCheckHospital.objects.filter(mtaInfoId=mta_info.id).filter(type=2)
        arrone =  list(mta_check_hospital_arr)
        arrtwo = list(un_mta_check_hospital_arr)
        # for result in mta_info:
        FileUtil.replaceDocxContent(mta_info, arrone, arrtwo)
    # results = MtaInfo.objects.filter(card="440506199601200728")
    # for result in results:
    #     FileUtil.replaceDocxContent(result)
    return JsonResponse({'message': 'User created successfully', "code": 200, "data": None})
