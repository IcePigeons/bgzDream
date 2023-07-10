import json

from django.forms import formset_factory
from django.http import HttpResponse

from docHandle.common import success_response
from docHandle.modelForm.CheckHospitalForm import CheckHospitalForm


def save_check_hospital(request):
    if request.method == 'POST':
        request.encoding = 'utf-8'
        # formset  = formset_factory(CheckHospitalForm, extra=1)(request.POST)
        data   = json.loads(request.body)
        print("很辉煌")
        # print(formset)
        # for form in formset:
        print(data )

    return success_response(None)