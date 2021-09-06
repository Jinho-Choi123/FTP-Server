from uuid import UUID
from rest_framework.views import APIView 
from fileupload.models import File, FileGroup
from fileupload.serializers import FileSerializer, FileGroupSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotAcceptable, NotFound
from django.http import FileResponse


class FileDownloadList(APIView):
    def get(self, request):
        try:
            groupid = request.query_params.get('gid')
            gid = UUID(groupid)
        except Exception as e:
            raise NotAcceptable(detail = 'GID Not Valid')
        files = File.objects.filter(group__gid = gid)
        if (not files.exists()):
            raise NotFound(detail = 'GID Not Found')
        ## filename, uid, filesize관련된 정보를 얻어오면 된다.
        serializer = FileSerializer(files, many=True)
        result = serializer.data
        return Response(result)

class FileDownload(APIView):
    def get(self, request):
        try:
            groupid = request.query_params.get('gid')
            uniqueid = request.query_params.get('uid')
            gid = UUID(groupid)
            uid = UUID(uniqueid)
            #get file that is corresponding to uid, gid
            file = File.objects.get(uid = uid, group = FileGroup.objects.get(gid = gid))
            f = open(file.content.path, 'rb')
            response = FileResponse(f)
            return response
        except Exception as e:
            raise NotAcceptable(detail = 'GID/UID Not Valid')
            