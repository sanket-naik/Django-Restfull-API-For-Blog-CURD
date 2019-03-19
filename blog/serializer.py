from rest_framework import serializers
from . import models

class blogSerializer(serializers.ModelSerializer):

    class Meta:
        fields=('id','name','title','content',)
        model=models.blog