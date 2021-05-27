from django.test import Client

from tasks.models import Category
from tasks.serializers import CategorySerializer


def test_tasks_create(db, client: Client) -> None:
    assert Category.objects.count() == 0
    data = {'title': 'daily'}
    serializer = CategorySerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    assert Category.objects.count() == 1
    assert Category.objects.first().title == 'daily'
