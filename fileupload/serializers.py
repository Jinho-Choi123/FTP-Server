from rest_framework import serializers 
from fileupload.models import File, FileGroup

# Serializer는 복잡한 데이터형식에서 데이터 추출을 도와준다. DB에 저장되어있는 데이터 <=> 필요한 데이터 추출!
# 간단히 말하자면 파이썬 객체와 JSON/XML 변환기를 Serializer라고 생각하면 된다.

class FileSerializer(serializers.Serializer):
    uid = serializers.UUIDField(
        format = 'hex'
    )
    gid = serializers.UUIDField(
        format = 'hex'
    )
    content = serializers.FileField(
        max_length = 40,
        allow_empty_file = False,
    )


class FileGroupSerializer(serializers.ModelSerializer):
    filelist = FileSerializer(read_only = True, many = True)
    class Meta:
        model = FileGroup
        fields = ['gid', 'expiredtime', 'filenum']