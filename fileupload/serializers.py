from rest_framework import serializers 

# Serializer는 복잡한 데이터형식에서 데이터 추출을 도와준다. DB에 저장되어있는 데이터 <=> 필요한 데이터 추출!
# 간단히 말하자면 파이썬 객체와 JSON/XML 변환기를 Serializer라고 생각하면 된다.

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = 