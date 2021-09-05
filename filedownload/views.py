from uuid import UUID
from django.shortcuts import render
from rest_framework.views import APIView 
from fileupload.models import File, FileGroup
from fileupload.serializers import FileSerializer, FileGroupSerializer
from rest_framework.response import Response


class FileDownload(APIView):
    def get(self, request):
        groupid = request.query_params.get('gid')
        gid = UUID(groupid)
        files = File.objects.filter(group__gid = gid)
        return Response("hello world")
        