from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from docHandle.models import MtaInfo
from docHandle.utils import FileUtil


# Create your api here.
def index(request):
    return render(request, "DocHandle.html")


def getDocx(request):
    response = HttpResponse("/static/docHandle/example2.docx")
    return response


def create_mta_info(request):
    print(request)
    if request.method == "POST":
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

        mta = MtaInfo(name=name, card=card, sex=sex, address=address, phone=phone, callTime=callTime,
                      policyNumber=policyNumber,
                      reportNumber=reportNumber, principalDate=principalDate, kindInsurance=kindInsurance,
                      dateInsurance=dateInsurance,
                      caseDesc=caseDesc, workMedicare=workMedicare, bodyHealth=bodyHealth, outpatient=outpatient,
                      hospital=hospital)
        mta.save()

    return JsonResponse({'message': 'User created successfully', "code": 200, "data": None})




