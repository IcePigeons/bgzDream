from django.http import HttpResponse
from django.shortcuts import render


# Create your api here.
def index(request):
    return render(request, "DocHandle.html")


def getDocx(request):
    response = HttpResponse("/static/docHandle/example2.docx")
    return response







