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
        gid = filegroup_.gid
        for file in files:
            file_ = File(gid = filegroup_, content = file)
            file_.group_id = gid
            filegroup_.addfile(file_)
            file_.save()
        filegroup_.save()
        filegroupserializer = FileGroupSerializer(filegroup_)
        expiredtime = filegroupserializer.data.expiredtime
        filenum = filegroupserializer.data.filenum
        filesize = filegroupserializer.data.filesize 
        gid = filegroupserializer.data.gid
        Response('Download link: localhost:8000/filedownload/{0}. expired time is {1}. number of file is {2}. total size of files is {3} '.format(gid, expiredtime, filenum, filesize))