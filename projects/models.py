from django.db import models
from users.models import profile
import uuid

# Create your models here.
class Project(models.Model):
    owner=models.ForeignKey(profile, null=True, blank=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    feature_image=models.ImageField(null=True, blank=True, default='default.jpg')
    demo_link=models.CharField(max_length=2000,null=True, blank=True)
    source_link=models.CharField(max_length=2000,null=True, blank=True)
    tags =models.ManyToManyField('tag', blank=True)
    total_vote=models.IntegerField(default=0, null=True, blank=True)
    vote_ratio=models.IntegerField(default=0, null=True, blank=True)
    created=models.DateTimeField(auto_now=True)
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    VOTE_TYPE=(
        ('up','Up Vote'),
        ('down', 'Down Vote'),
    )
    project = models.ForeignKey('Project', on_delete=models.CASCADE )
    body=models.TextField(null=True, blank=True)
    value=models.CharField(max_length=200, choices=VOTE_TYPE)
    created=models.DateTimeField(auto_now=True)
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.value 
    
class Tag(models.Model):
    name= models.CharField(max_length=200)
    created=models.DateTimeField(auto_now=True)
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name
    
class Userm(models.Model):
        name=models.CharField(max_length=200)
        email=models.EmailField(unique=True)
        id=models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
        def __str__(self):
            return self.name






