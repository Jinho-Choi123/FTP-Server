from rest_framework import serializers 
from fileupload.models import File, FileGroup
from uuid import UUID

# Serializer는 복잡한 데이터형식에서 데이터 추출을 도와준다. DB에 저장되어있는 데이터 <=> 필요한 데이터 추출!
# 간단히 말하자면 파이썬 객체와 JSON/XML 변환기를 Serializer라고 생각하면 된다.

class FileSerializer(serializers.ModelSerializer):
    filename = serializers.SerializerMethodField()
    filesize = serializers.SerializerMethodField()
    uid = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()

    def get_group(self, file):
        group_hex = file.group.gid.hex
        return group_hex

    def get_uid(self, file):
        uid_hex = file.uid.hex 
        return uid_hex

    def get_filename(self, file):
        filepath = file.content.name
        filename = filepath.split('/')[1]
        return filename


    def get_filesize(self, file):
        return file.content.size    
    class Meta:
        model = File 
        fields = '__all__'


class FileGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileGroup
        fields = '__all__'