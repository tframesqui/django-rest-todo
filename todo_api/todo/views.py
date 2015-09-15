from rest_framework import viewsets

from .models import Todo,Item

from .serializers import TodoSerializer, ItemSerializer



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    items = ItemViewSet