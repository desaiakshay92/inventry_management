from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from consumables.models import Items, NewItem, DeletedItems

class ItemSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"

class NewItemSerilizer(serializers.ModelSerializer):
    item = ItemSerilizer(many=True, read_only=True)
    class Meta:
        model = NewItem
        fields = "__all__"

class DeletedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeletedItems
        fields = "__all__"

