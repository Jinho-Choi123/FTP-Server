from django.db import models
import datetime 
import uuid

def hex_uuid():
    return uuid.uuid4().hex

#File Group contains attr of list of File Obj
class FileGroup(models.Model):
    gid = models.UUIDField(
        primary_key=True,
        default = hex_uuid,
        editable = False,
    )
    uploadtime = models.DateTimeField(auto_now_add = True)

    expiredtime = models.DateTimeField(null = False, default = datetime.datetime.now() + datetime.timedelta(hours = 6))
    filenum = models.PositiveIntegerField(default = 0)
    filesize = models.PositiveBigIntegerField(default = 0)
    def addfile(self, file):
        self.filenum = self.filenum + 1 
        file_size = file.content.size
        self.filesize = self.filesize + file_size

def file_dir_path(instance, filename):
    return '{0}/{1}'.format(instance.group.gid, filename)

class File(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default = hex_uuid,
        editable = False,
    )
    group = models.ForeignKey(FileGroup, related_name='filelist', on_delete=models.CASCADE, db_constraint= False, blank = True)
    content = models.FileField(max_length = 200, blank = False, null = True, upload_to = file_dir_path)