from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User 
from datetime import datetime 
from pytz import timezone

class Monitor(APIView):
    def get(self, request, format = None):
        KST = datetime.now(timezone('ASIA/Seoul')).strftime('%Y-%m-%d %H:%M:%S')
        stat = 'Server is Alive. Current KST is {}'.format(KST)
        return Response(stat)