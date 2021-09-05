from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import File, FileGroup 
from .serializers import FileSerializer, FileGroupSerializer
from rest_framework.parsers import MultiPartParser, FormParser
import uuid

####Logging
import logging
logger = logging.getLogger(__name__)

class FileUpload(APIView):
    def post(self, request):
        #files is list of file object
        files = request.FILES.getlist('uploadfile')
        filegroup_ = FileGroup()
        gid = filegroup_.gid 
        gid = gid.int
        logger.error('@@@@@@@@@@@@@@@@@@@@@@@@@GID is {}'.format(gid))
        logger.error(files)

        for file in files:
            logger.error("##################file name is {}".format(file.name))
            file_ = File(group = filegroup_, content = file)
            logger.error("$$$$$$$$$$$ made a file object")
            filegroup_.addfile(file_)
            logger.error("%%%%%%%%%%%%%%%%%%%%add file to filegroup obj")
            file_.save()
            logger.error("&&&&&&&&&&&&&&&&&save file obj to DB")
        filegroup_.save()
        filegroupserializer = FileGroupSerializer(filegroup_)
        filegroupData= filegroupserializer.data
        logger.error(filegroupData)
        return Response("hello world")