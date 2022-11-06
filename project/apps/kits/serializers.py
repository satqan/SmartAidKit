from rest_framework import serializers
from .models import Kit
from apps.drugs.serializers import DrugSerializer


class KitSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    drugs = DrugSerializer(many=True, read_only=True)

    class Meta:
        model = Kit
        fields = '__all__'
