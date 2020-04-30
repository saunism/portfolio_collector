from django.db import models

class Portfolio(models.Model):
    author_full_name = models.CharField(max_length=150,null=True)
    author_id = models.IntegerField()
    city = models.CharField(max_length=50,null=True)
    profession = models.CharField(max_length=50,null=True)
    experience = models.IntegerField()
    education = models.CharField(max_length=100,null=True)
    discription = models.TextField(null=True)
    sertificate = models.TextField(null=True)
