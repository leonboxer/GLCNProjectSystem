from rest_framework import serializers
from .models import User, Role


# Serializers define the API representation.
class RoleSerializer(serializers.ModelSerializer):
    # id = serializers.CharField(source='get_id_display')
    # id = serializers.CharField()
    # id = 'test'
    class Meta:
        model = Role
        fields = ['id']


class UserSerializer(serializers.ModelSerializer):
    # roles = RoleSerializer(read_only=True, many=True)
    # roles = ['test']
    # roles=serializers.MultipleChoiceField(choices='id')
    roles = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        # fields = ['roles']
        fields = ['name', 'email', 'roles', 'avatar']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model = Group
        fields = ['url', 'name']
