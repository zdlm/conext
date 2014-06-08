from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class QA(models.Model):
    title = models.CharField(max_length=500,blank=True)
    content = models.TextField(max_length=10000)
    company = models.CharField(max_length=100,blank=True)#should be ForeignKey, change later
    tags = models.CharField(max_length=200,blank=True)
    categary = models.CharField(max_length=200,blank=True)#tester,designer,developer....
    topic = models.CharField(max_length=200,blank=True)
    at_who = models.CharField(max_length=200,blank=True)#should be ForeignKey, change later
    vote_count = models.IntegerField()
    answer_count = models.IntegerField()
    like_count = models.IntegerField()
    dislike_count = models.IntegerField()
    keep_count = models.IntegerField()
    delete_count = models.IntegerField()
    stars = models.IntegerField()#0-5
    tags = models.CharField(max_length=200,blank=True)
    type=models.CharField(max_length=50)#question or answer
    is_duplicate=models.BooleanField(default=False)#for question
    duplicate_ids=models.CharField(max_length=200)#question id seperate by ,
    created_by = models.CharField(max_length=200)#models.ForeignKey(User)
    updated_by = models.CharField(max_length=200)#models.ForeignKey(User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
