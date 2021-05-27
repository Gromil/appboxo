from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True
    )


class Task(models.Model):
    DONE = 'done'
    FAILED = 'failed'
    ACTIVE = 'active'

    STATES = (
        (DONE, 'done'),
        (FAILED, 'failed'),
        (ACTIVE, 'active')
    )

    title = models.CharField(max_length=225)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.CharField(choices=STATES, default=ACTIVE, max_length=10)
