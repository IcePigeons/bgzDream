"""
URL configuration for bgzDream project.

The `urlpatterns` list routes URLs to api. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function api
    1. Add an import:  from my_app import api
    2. Add a URL to urlpatterns:  path('', api.home, name='home')
Class-based api
    1. Add an import:  from other_app.api import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from docHandle.api.hospital import list_hospital
from docHandle.api.mta import save_check_hospital, download_mta
from docHandle.views import create_mta_info, index,getDocx

urlpatterns = [
    path('doc/', index),
    path('getDocx/', getDocx),
    path('create_mta_info/', create_mta_info, name="create_mta_info"),
    path('download_mta/', download_mta, name="download_mta"),

    path('list_hospital/', list_hospital, name="list_hospital"),
    path('save_check_hospital/', save_check_hospital,name="save_check_hospital"),
]
