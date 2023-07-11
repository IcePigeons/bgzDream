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







