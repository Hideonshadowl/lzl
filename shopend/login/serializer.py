from rest_framework import serializers
from .models import *
class bloginfoModelSerializers(serializers.ModelSerializer):
    class Meta:
        model =bloginfo
        fields = '__all__'
class AuthorModelSerializers(serializers.ModelSerializer):
    class Meta:
        model =Author
        fields = '__all__'