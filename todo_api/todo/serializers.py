from rest_framework import serializers

from .models import Todo, Item

class TodoSerializer(serializers.HyperlinkedModelSerializer):
	items = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="todo_detail")

	class Meta:
		model = Todo
		fields = ('id', 'name', 'slug', 'pub_date', 'items')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'name', 'done')