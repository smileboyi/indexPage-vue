# from django.shortcuts import HttpResponse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
import json
from . import models

# Create your views here.


# 转成哈希值
def hash_code(s, salt='webapp'):
  s += salt        # 加点盐
  return make_password(ps, None, 'pbkdf2_sha256')



@require_http_methods(["GET"])
def gift_list(request):
  level = request.GET.get('level')

  # 每个价格区间都有一个大礼品，在前端，第一个展示的是大礼品
  first_big_gift = models.Gift.objects.filter(is_range_great__exact=1, price_range__exact=level).values(
    'pic_url', 'title','parameter','market_price','discount_price','price_range')
  datas = [list(first_big_gift)[0],]
    
  # 剩下的礼品
  # gift = models.Gift.objects.all().values('pic_url', 'title','parameter','market_price','discount_price','price_range')
  # for i in list(gift):
  #   print(gift[i])

  print(datas)
  result = {}
  result["datas"] = datas
  return JsonResponse(result,safe=False)


@require_http_methods(["GET"])
def hr_list(request):
  hr = serializers.serialize("json", models.Hr.objects.all())
  result = {}
  result["datas"] = hr
  return HttpResponse(json.dumps(result), content_type="application/json")