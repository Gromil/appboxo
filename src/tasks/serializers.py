from rest_framework.serializers import ModelSerializer

from tasks.models import Category, Task


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'parent')


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'category', 'state')
