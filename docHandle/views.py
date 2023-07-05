from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from docHandle.models import MtaInfo


# Create your views here.
def index(request):
    return render(request, "DocHandle.html")


def getDocx(request):
    response = HttpResponse("C:\\Users\\77172\\Desktop\\example2.docx")
    return response


def create_mta_info(request):
    if request.method == "POST":
        mid = request.POST.get("id")
        name = request.POST.get("name")
        card = request.POST.get("card")
        mta = MtaInfo(mid=mid, name=name, card=card)
        mta.save()
    return JsonResponse({'message': 'User created successfully'})
