from django.test import Client
from requests import Response

from tasks.models import Category


def test_tasks_get(db, client: Client) -> None:
    assert Category.objects.count() == 0
    response: Response = client.post(
        path='/api/category/', data={'title': 'dadada'}
    )
    assert response.json() == {'title': 'dadada', 'parent': None}
    assert response.status_code == 201
    assert Category.objects.count() == 1
