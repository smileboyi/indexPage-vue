# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Account(models.Model):
  nickname = models.CharField(max_length=32)
  account_tel = models.CharField(max_length=128)
  password = models.CharField(max_length=64)
  add_time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.nickname


class Hr(models.Model):
  pic_url = models.CharField(max_length=256)
  viedeo_src = models.CharField(max_length=256)
  name = models.CharField(max_length=32)
  sex = models.IntegerField(choices=(
    (1,"男"),
    (2,"女"),
  ),verbose_name="性别")
  join_datetime = models.DateTimeField(auto_now_add=True)
  text = models.CharField(max_length=256)
  download_num = models.IntegerField()
  share_num = models.IntegerField()
  convert_num = models.IntegerField()
  gift_value = models.FloatField()



class Gift(models.Model):
  pic_url = models.CharField(max_length=256)
  title = models.CharField(max_length=64)
  parameter = models.CharField(max_length=256)
  market_price = models.IntegerField()
  discount_price = models.IntegerField()
  is_range_great = models.BooleanField()
  price_range = models.CharField(max_length=64, choices=(
    ('1wup', '10000以上'),
    ('8kup', '8000以上'),
    ('6kup', '6000以上'),
    ('4kup', '4000以上'),
    ('3kup', '3000以上'),
    ('2kup', '2000以上'),
    ('1kup', '1000以上'),
    ('1kdown', '1000以下'),    
  ))
