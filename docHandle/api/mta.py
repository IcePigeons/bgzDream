import json
import os.path

from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse

from docHandle.common import success_response, error_response
from docHandle.models import MtaCheckHospital, MtaInfo, MtaConclusion
from docHandle.utils import FileUtil


# 保存/更新排查医院信息
def save_check_hospital(request):
    if request.method == 'POST':
        request.encoding = 'utf-8'
        data = json.loads(request.body)
        for obj in data:
            if obj['id']  != -1:  # 更新
                if obj['type'] == 1:
                    MtaCheckHospital.objects.filter(id=obj['id']) \
                        .update(hospitalName=obj['hospitalName'], hospitalAddress=obj['hospitalAddress'],
                                checkDate=obj['checkDate'],
                                userInfo=obj['userInfo'], outpatientNumber=obj['outpatientNumber'],
                                hospitalNumber=obj['hospitalNumber'],
                                hospitalStayId=obj['hospitalStayId'], outpatientRecord=obj['outpatientRecord'],
                                hospitalStayFirst=obj['hospitalStayFirst'],
                                mainSymptom=obj['mainSymptom'], medicalHistory=obj['medicalHistory'],
                                dischargeDiagnosis=obj['dischargeDiagnosis'],
                                previousHistory=obj['previousHistory'],
                                remark=obj['remark'], otherHospitalInfo=obj['otherHospitalInfo'],
                                type=obj['type'], mtaInfoId=obj['mtaInfoId'])
                else:
                    MtaCheckHospital.objects.filter(id=obj['id']) \
                        .update(hospitalName=obj['hospitalName'], hospitalAddress=obj['hospitalAddress'],
                                checkDate=obj['checkDate'],
                                userInfo=obj['userInfo'], remark=obj['remark'],
                                checkContent=obj['checkContent'],
                                type=obj['type'], mtaInfoId=obj['mtaInfoId'])
            else:  # 新增
                if obj['type'] == 1:
                    mch = MtaCheckHospital(hospitalName=obj['hospitalName'], hospitalAddress=obj['hospitalAddress'],
                                           checkDate=obj['checkDate'],
                                           userInfo=obj['userInfo'], outpatientNumber=obj['outpatientNumber'],
                                           hospitalNumber=obj['hospitalNumber'],
                                           hospitalStayId=obj['hospitalStayId'],
                                           outpatientRecord=obj['outpatientRecord'],
                                           hospitalStayFirst=obj['hospitalStayFirst'],
                                           mainSymptom=obj['mainSymptom'], medicalHistory=obj['medicalHistory'],
                                           dischargeDiagnosis=obj['dischargeDiagnosis'],
                                           previousHistory=obj['previousHistory'],
                                           remark=obj['remark'], otherHospitalInfo=obj['otherHospitalInfo'],
                                           type=obj['type'], mtaInfoId=obj['mtaInfoId'])
                    mch.save()
                else:
                    mch = MtaCheckHospital(hospitalName=obj['hospitalName'], hospitalAddress=obj['hospitalAddress'],
                                           checkDate=obj['checkDate'],
                                           userInfo=obj['userInfo'], remark=obj['remark'],
                                           checkContent=obj['checkContent'],
                                           type=obj['type'], mtaInfoId=obj['mtaInfoId'])
                    mch.save()
    return success_response(None)


def delete_check_hospital(request):
    if request.method == 'GET':
        id_key = request.GET.get("id")
        try:
            MtaCheckHospital.objects.get(id=id_key).delete()
        except Exception as error:
            # 处理异常
            return error_response("删除失败："+error)
        return success_response(None)


# 新增/更新基础信息
def create_mta_info(request):
    print(request)
    if request.method == "POST":
        id_key = request.POST.get("id")
        name = request.POST.get("name")
        card = request.POST.get("card")
        sex = request.POST.get("sex")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        callTime = request.POST.get("callTime")
        policyNumber = request.POST.get("policyNumber")
        reportNumber = request.POST.get("reportNumber")
        principalDate = request.POST.get("principalDate")
        kindInsurance = request.POST.get("kindInsurance")
        dateInsurance = request.POST.get("dateInsurance")
        caseDesc = request.POST.get("caseDesc")
        workMedicare = request.POST.get("workMedicare")
        bodyHealth = request.POST.get("bodyHealth")
        outpatient = request.POST.get("outpatient")
        hospital = request.POST.get("hospital")
        if id_key is not None:  # 更新
            MtaInfo.objects.filter(id=id_key) \
                .update(name=name, card=card, sex=sex, address=address, phone=phone,
                        callTime=callTime, policyNumber=policyNumber,
                        reportNumber=reportNumber,
                        principalDate=principalDate, kindInsurance=kindInsurance,
                        dateInsurance=dateInsurance,
                        caseDesc=caseDesc, workMedicare=workMedicare,
                        bodyHealth=bodyHealth, outpatient=outpatient,
                        hospital=hospital)

        else:
            mta = MtaInfo(name=name, card=card, sex=sex, address=address, phone=phone, callTime=callTime,
                          policyNumber=policyNumber, reportNumber=reportNumber, principalDate=principalDate,
                          kindInsurance=kindInsurance, dateInsurance=dateInsurance, caseDesc=caseDesc,
                          workMedicare=workMedicare, bodyHealth=bodyHealth, outpatient=outpatient,
                          hospital=hospital)
            mta.save()

    return JsonResponse({'message': 'User created successfully', "code": 200, "data": None})


# 导出结果文件
def download_mta(request):
    if request.method == "POST":
        body = json.loads(request.body)
        id_key = body.get("params").get("id")
        # card = request.POST.get("card")
        mta_info = MtaInfo.objects.filter(id=id_key).first()
        mta_check_hospital = MtaCheckHospital.objects.filter(mtaInfoId=mta_info.id).filter(type=1)
        un_mta_check_hospital = MtaCheckHospital.objects.filter(mtaInfoId=mta_info.id).filter(type=2)
        mta_conclusion = MtaConclusion.objects.filter(mtaInfoId=mta_info.id).first()
        # 转为列表
        mta_check_hospital_arr = list(mta_check_hospital)
        un_mta_check_hospital_arr = list(un_mta_check_hospital)
        filepath = FileUtil.replaceDocxContent(mta_info, mta_check_hospital_arr, un_mta_check_hospital_arr,
                                               mta_conclusion)

        # 返回文件
        response = HttpResponse(read_file(filepath))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(filepath)
        if response is not None:
            return response
        else:
            return error_response("访问失败")


def read_file(url, chunk_size=512):
    with open(url, "rb") as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


# 获取用户列表信息
def get_user_info(request):
    all_obj = MtaInfo.objects.all().values("id", "card", "name")
    # 返回json
    return success_response(list(all_obj))


# 获取全部整体信息
def get_all_info(request):
    if request.method == "GET":
        id_key = request.GET.get("id")
        mta_info = MtaInfo.objects.get(id=id_key)
        check_hospital = MtaCheckHospital.objects.all()
        conclusion = MtaConclusion.objects.get(mtaInfoId=id_key)
        data = {
            "mtaInfo": model_to_dict(mta_info),
            "checkHospital": serializers.serialize("json", check_hospital),
            "conclusion": model_to_dict(conclusion)
        }

        return success_response(data)


# 获取结论
def get_mta_conclusion(request):
    if request.method == "GET":
        id_key = request.GET.get("id")
        all_obj = MtaConclusion.objects.get(id=id_key)
        return JsonResponse({'message': 'User created successfully', "code": 200, "data": all_obj})


# 更新/新增结论
def save_mta_conclusion(request):
    if request.method == "POST":
        data = json.loads(request.body)
        id_key = data.get("id")
        add_mta_conclusion(id_key, data)
    return success_response(None)


def add_mta_conclusion(id_key: int, data):
    if id_key is not None:  # 更新
        MtaConclusion.objects.filter(id=id_key) \
            .update(accidentHospital=data.get('accidentHospital'),
                    hospitalTimeRange=data.get('hospitalTimeRange'),
                    dischargeDiagnosis=data.get('dischargeDiagnosis'), editDate=data.get('editDate'),
                    recheck=data.get('recheck'),
                    survey=data.get('survey'), mtaInfoId=data.get('mtaInfoId'))
    else:
        MtaConclusion(accidentHospital=data.get('accidentHospital'),
                      hospitalTimeRange=data.get('hospitalTimeRange'),
                      dischargeDiagnosis=data.get('dischargeDiagnosis'), editDate=data.get('editDate'),
                      recheck=data.get('recheck'),
                      survey=data.get('survey'), mtaInfoId=data.get('mtaInfoId')).save()
