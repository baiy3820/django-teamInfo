from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Teamer(models.Model):
    english_name = models.CharField(max_length=64)
    Chinese_name = models.CharField(max_length=16)
    sex = models.CharField(max_length=8)
    Birthday = models.DateTimeField('Birthday')
    phone = models.CharField(max_length=64)
    hobby = models.CharField(max_length=200)
    position = models.CharField(max_length=64)
    dayily_voice = models.CharField(max_length=200)

    def __str__(self):
        return self.dayily_voice

    def was_birthday_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.Birthday <= now
    was_birthday_recently.admin_order_field = 'Birthday'
    was_birthday_recently.boolean = True 
    was_birthday_recently.short_description = 'Birthday Recently?'

class Choice(models.Model):
    teamer = models.ForeignKey(Teamer)
    choice_reason = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 
    
    def __str__(self):
        return self.choice_reason
