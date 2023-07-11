import os.path
import string
import uuid
from array import array

from docxtpl import DocxTemplate

from docHandle.models import MtaInfo, MtaCheckHospital


class FileUtil:
    # 民太安模板内容docx内容替换
    @staticmethod
    def replaceDocxContent(mtaInfo: MtaInfo, mtaCheckHospitalArr: list, mtaUnCheckHospitalArr: list):
        # print(os.path.abspath("DocxTemplate/mta-template.docx"))
        doc = DocxTemplate(os.path.abspath("DocxTemplate/mta-template.docx"))  # 选定模板
        # 需要替换的内容
        context = {
            'name': mtaInfo.name,
            'card': mtaInfo.card,
            'sex': mtaInfo.sex,
            'address': mtaInfo.address,
            'phone': mtaInfo.phone,
            'callTime': mtaInfo.callTime,
            'policyNumber': mtaInfo.policyNumber,
            'reportNumber': mtaInfo.reportNumber,
            'principalDate': mtaInfo.principalDate,
            'kindInsurance': mtaInfo.kindInsurance,
            'dateInsurance': mtaInfo.dateInsurance,
            'caseDesc': mtaInfo.caseDesc,
            'workMedicare': mtaInfo.workMedicare,
            'bodyHealth': mtaInfo.bodyHealth,
            'outpatient': mtaInfo.outpatient,
            'hospital': mtaInfo.hospital,
            'outpatientNum': count(mtaInfo.outpatient),  # 门诊次数统计
            'hospitalNum': count(mtaInfo.hospital),  # 住院次数统计
            'lifeTrackInfo': mtaInfo.lifeTrackInfo,
            'location': mtaInfo.address[:9],  # 所在地
            # 排查医院信息数组
            'mtaCheckHospitalArr': mtaCheckHospitalArr,
            'mtaUnCheckHospitalArr': mtaUnCheckHospitalArr,
            # 'hospitalName': mtaCheckHospital.hospitalName,
            # 'hospitalAddress': mtaCheckHospital.hospitalAddress,
            # 'checkDate': mtaCheckHospital.checkDate,
            # 'userInfo': mtaCheckHospital.userInfo,
            # 'outpatientNumber': mtaCheckHospital.outpatientNumber,
            # 'hospitalNumber': mtaCheckHospital.hospitalNumber,
            # 'hospitalStayId': mtaCheckHospital.hospitalStayId,
            # 'outpatientRecord': mtaCheckHospital.outpatientRecord,
            # 'hospitalStayFirst': mtaCheckHospital.hospitalStayFirst,
            # 'mainSymptom': mtaCheckHospital.mainSymptom,
            # 'medicalHistory': mtaCheckHospital.medicalHistory,
            # 'previousHistory': mtaCheckHospital.previousHistory,
            # 'dischargeDiagnosis': mtaCheckHospital.dischargeDiagnosis,
            # 'remark': mtaCheckHospital.remark,
            # 'otherHospitalInfo': mtaCheckHospital.otherHospitalInfo,
            # 'type': mtaCheckHospital.type,
        }
        doc.render(context)  # 渲染替换
        doc.save("DocxTemplate/out/" + mtaInfo.name + "-调查报告 民太安.docx")  # 保存


def count(s: str):
    return s.count("、")
