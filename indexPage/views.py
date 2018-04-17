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
  gift = models.Gift.objects.values('pic_url', 'title','parameter','market_price','discount_price','is_range_great','price_range')
  print(list(gift))
  result = {}
  result["datas"] = 333
  return JsonResponse(result,safe=False)


@require_http_methods(["GET"])
def hr_list(request):
  hr = serializers.serialize("json", models.Hr.objects.all())
  result = {}
  result["datas"] = hr
  return HttpResponse(json.dumps(result), content_type="application/json")