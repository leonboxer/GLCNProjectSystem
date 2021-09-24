from rest_framework import serializers
from .models import Element


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ('id', 'tag', 'material', 'created', 'updated')
