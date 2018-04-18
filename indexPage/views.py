# from django.shortcuts import HttpResponse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import make_password, check_password
import json
from . import models

# Create your views here.


# 转成哈希值
def hash_code(s, salt='webapp'):
  s += salt        # 加点盐
  return make_password(ps, None, 'pbkdf2_sha256')


# 用户注册
@require_http_methods(["POST"])
def register(request):
  # if request.method == "POST":
  #   tel = request.POST.get('tel')
  #   code = request.POST.get('code')
  #   print(tel,code)

  #   same_account = models.Account.objects.filter(account_tel=tel)
  #   if same_account:  # 手机号唯一
  #     return JsonResponse({error: "手机号已被注册"},safe=False)

  #   # 满足条件，创建新用户
  #   new_account = models.Account.objects.create()
  #   new_account.account_tel = tel
  #   new_account.password = hash_code(123456)
  #   new_account.save()

  #   return JsonResponse({info: "注册成功，初始密码为123456"},safe=False)

  return JsonResponse({error: "请求失败"},safe=False)



@require_http_methods(["GET"])
def gift_list(request):
  level = request.GET.get('level')

  # 每个价格区间都有一个大礼品，在前端，第一个展示的是大礼品
  first_big_gift = models.Gift.objects.filter(is_range_great__exact=1, price_range__exact=level).values(
    'id','pic_url','title','parameter','market_price','discount_price')
  datas = [list(first_big_gift)[0],]
    
  # 剩下的礼品(7个)
  gift = models.Gift.objects.filter(is_range_great__exact=0, price_range__exact=level)[:7].values(
    'id','pic_url','title','parameter','market_price','discount_price')
  for item in gift:
    datas.append(item)

  # 返回给前端
  result = {}
  result["datas"] = datas
  return JsonResponse(result,safe=False)



@require_http_methods(["GET"])
def hr_list(request):
  hr = models.Hr.objects.all()[:12].values('id','pic_url','viedeo_src','name','sex','join_datetime','text','download_num','share_num','convert_num','gift_value')
  # 构造响应数据结构
  datas = []
  for item in hr:
    outer_dict = {}
    inter_dict = {}

    outer_dict['pic_url'] = item['pic_url']
    outer_dict['viedeo_src'] = item['viedeo_src']

    inter_dict['id'] = item['id']
    inter_dict['name'] = item['name']
    inter_dict['sex'] = item['sex']
    inter_dict['text'] = item['text']
    inter_dict['download_num'] = item['download_num']
    inter_dict['share_num'] = item['share_num']
    inter_dict['convert_num'] = item['convert_num']
    inter_dict['gift_value'] = item['gift_value']
    inter_dict['join_year'] = item['join_datetime'].strftime('%Y')

    outer_dict['details'] = inter_dict
    datas.append(outer_dict)

  result = {}
  result["datas"] = datas

  # 换一种方式返回json
  return HttpResponse(json.dumps(result), content_type="application/json")