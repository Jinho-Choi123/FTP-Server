import datetime
from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import File, FileGroup 
from .serializers import FileSerializer, FileGroupSerializer
from rest_framework.parsers import MultiPartParser, FormParser
import uuid

class FileUpload(APIView):
    def post(self, request):
        #files is list of file object
        files = request.FILES.getlist('uploadfile')
        filegroup_ = FileGroup()
        for file in files:
            file_ = File(group = filegroup_, content = file)
            filegroup_.addfile(file_)
            file_.save()
        filegroup_.save()
        filegroupserializer = FileGroupSerializer(filegroup_)
        filegroupData= filegroupserializer.data
        return Response(filegroupData)