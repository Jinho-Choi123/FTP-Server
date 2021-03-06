"""ftp_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from checkserver.views import Monitor
from fileupload.views import FileUpload
from filedownload.views import FileDownloadList, FileDownload

urlpatterns = [
    path('checkserver/', Monitor.as_view(), name="checkserver"),
    path('fileupload/', FileUpload.as_view(), name="fileupload"),
    path('filedownload/list/', FileDownloadList.as_view(), name = "filedownloadlist"),
    path('filedownload/', FileDownload.as_view(), name='filedownload'),
]