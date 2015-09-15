from django.db import models

# Create your models here.
class Todo(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    pub_date = models.DateTimeField()

class Item(models.Model):
    def __str__(self):
        return self.name

    todo = models.ForeignKey(Todo)
    name = models.CharField(max_length=200)
    done = models.BooleanField()