from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.permissions import SAFE_METHODS,BasePermission

# Create your models here.
class Envelope(models.Model):
    school_code=models.CharField(max_length=32)
    date_due=models.DateTimeField()
    exam_start=models.DateTimeField()
    exam_duration=models.IntegerField(default=90)
    editors=models.ManyToManyField(User,related_name="admins")
    owner=models.ForeignKey('auth.User',related_name="the_creator")

class EnvelopeSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Envelope
        fields=('id','school_code','date_due','exam_start','exam_duration','owner_name','owner','editors')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        field=('username','id')

class IsEditor(BasePermission):
    message = 'Toka Hapa.'
    def has_object_permission(self, request, view, obj):
        #if request.method in SAFE_METHODS:
        #     return True
        # if request.user in obj.editors:
        #     return True
        #print EnvelopeSerializer(obj).data['editors']
        #print request.user.id

        if request.user.id in EnvelopeSerializer(obj).data['editors'] or obj.owner ==request.user:
            return True
        else:
            return False
