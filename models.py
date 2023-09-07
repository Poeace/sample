from django.db import models

# Create your models here.
from django.db import models


class course_detail(models.Model):

    cid = models.CharField(max_length=10)
    c_name = models.CharField(max_length=40)
    aff_uni = models.CharField(max_length=60)
    seats = models.CharField(max_length=60)
    fees = models.CharField(max_length=40)
    pattern = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)

    class Meta:
        db_table = "course_detail"

class teacher(models.Model):

    tid = models.CharField(max_length=10)
    tname = models.CharField(max_length=60)
    tcont = models.CharField(max_length=15)
    tadd = models.CharField(max_length=40)
    tquali = models.CharField(max_length=20)
    tdept = models.CharField(max_length=10)
    tj_date = models.CharField(max_length=15)
    texp = models.CharField(max_length=15)
    tsal = models.CharField(max_length=15)

    class Meta:
        db_table = "teacher"
