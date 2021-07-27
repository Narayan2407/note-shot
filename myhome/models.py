from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

class sem(models.Model):
    name=models.CharField(max_length=30)
    sem_id=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name

class course(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    cid=models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to ='myhome/static/all_images', blank=True)
    category_id=models.IntegerField()

    def __str__(self):
        return self.name

class course_pdf(models.Model):
    pdf_file = models.FileField(upload_to ='myhome/static/all_pdf',blank=True)
    pdf_name=models.CharField(primary_key=True,db_index=True,max_length=30)
    course_id=models.ForeignKey(course,on_delete=models.CASCADE)
    ccid=models.IntegerField(default=0)

    def __str__(self):
        return self.pdf_name



