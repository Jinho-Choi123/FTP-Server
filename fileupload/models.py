from django.db import models
import datetime 
import uuid
# Create your models here.
class File:
    def __init(self, filename, ):
        self.filename = filename 
        self.uploadtime = datetime.datetime.now()
        self.expiredtime = datetime.datetime.now() + datetime.timedelta(hours = 6)
        self.uid = uuid.uuid4()
        

