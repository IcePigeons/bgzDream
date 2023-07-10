import json

from django.db import models

from docHandle.common import success_response
from docHandle.models import Hospital

from django.http import JsonResponse


def list_hospital(request):
    if request.method == 'GET':
        result = Hospital.objects.all()
        return success_response(list(result.values()))
