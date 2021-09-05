from django.db import models
import datetime 
import uuid

#File Group contains attr of list of File Obj
class FileGroup(models.Model):
    gid = models.UUIDField(
        primary_key=True,
        default = uuid.uuid4,
        editable = False
    )
    uploadtime = models.DateTimeField(auto_now_add = True)
    expiredtime = models.DateTimeField(null = True)
    filenum = models.PositiveIntegerField(default = 0)
    filesize = models.PositiveBigIntegerField(default = 0)
    def __init(self):
        self.gid = uuid.uuid4()
        #after expiredtime, the file will be nonactive.
        self.expiredtime = datetime.datetime.now() + datetime.timedelta(hours = 6)
        #info of the numbers of files & total size of files. 
        self.filenum = 0
        self.filesize = 0
    def addfile(self, file):
        self.filenum = self.filenum + 1 
        file_size = file.content.size
        self.filesize = self.filesize + file_size


class File(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        default = uuid.uuid4,
        editable = False
    )
    group = models.ForeignKey(FileGroup, related_name='filelist', on_delete=models.CASCADE, db_constraint= False, blank = True)
    content = models.FileField(max_length = 40, blank = False, null = True)

    #initialize with filename, extension and groupid
    def __init(self, group, content):
        self.content = content
        self.group = group 
        #store path is <basepath>/gid/uid  저장 이름은 uid. 실제 이름은 filename.