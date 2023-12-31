from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import profile


def profileCreate(sender,instance,created, **kwargs):
    if created:
        user=instance
        createprofile=profile.objects.create(
            user=user,
            name=user.name,
            username=user.username,
            email=user.email,
        )
    
def deleteUser(sender,instance,**kwargs):
    user=instance.user
    user.delete()

post_save.connect(profileCreate,sender=User)
post_delete.connect(deleteUser,sender=profile)