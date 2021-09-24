from rest_framework import serializers

from .models import Material


class MaterialSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    class Meta:
        model = Material
        fields = ('id', 'material_number', 'order_number', 'brand', 'type', 'created', 'updated')
