from ftp_server.settings import BASE_DIR
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import File, FileGroup
from .serializers import FileGroupSerializer, FileSerializer

import logging
logger = logging.getLogger(__name__)

class FileUploadTestCase1(APITestCase):

    def test_fileupload(self):
        with open(BASE_DIR/'testfiles/video1.mp4', 'rb') as video1, open(BASE_DIR/'testfiles/video2.mp4', 'rb') as video2, open(BASE_DIR/'testfiles/image1.jpg', 'rb') as image1:
            files = {
                'uploadfile': video1,
                'uploadfile': video2,
                'uploadfile': image1,
                }
            response = self.client.post("/fileupload/", files = files, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_200_OK)