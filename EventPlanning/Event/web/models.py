from django.contrib.auth.models import AbstractUser
from django.db import models
class Buyer(AbstractUser):
    ...

class Events(models.Model):
    title = models.CharField('Название мероприятия', max_length=25)
    name = models.CharField('Название собятия', max_length=25)
    place = models.CharField('Место', max_length=50)
    start_at = models.CharField('Начало', max_length=5)
    end_at = models.CharField('Конец', max_length=5)
    full_text = models.TextField('Описание')
    web_buyer_id = models.IntegerField()

    def __str__(self):
        return self.title


class UserHasEvent(models.Model):
    title_events = models.CharField('Название мероприятия', max_length=25)
    web_buyer_id = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_events