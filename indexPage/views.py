from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
import datetime
from . import check_code
from . import models
import json
import io

# Create your views here.


# 转成哈希值
def hash_code(ps, salt='webapp'):
  ps += salt        # 加点盐
  return make_password(ps, None, 'pbkdf2_sha256')



# 验证码
def create_code_img(request):
  f = io.BytesIO() #直接在内存开辟一点空间存放临时生成的图片
  img, code = check_code.create_validate_code() #调用check_code生成照片和验证码
  request.session['check_code'] = code #将验证码存在服务器的session中，用于校验
  img.save(f,'PNG') #生成的图片放置于开辟的内存中
  return HttpResponse(f.getvalue(), 'image/png')  #将内存的数据读取出来，并以HttpResponse返回



# 用户注册
@csrf_exempt
@require_http_methods(["POST"])
def register(request):
  if request.method == "POST":
    # 获取用户数据
    tel = request.POST.get('tel')
    code = request.POST.get('code')
    check_code = request.session['check_code']

    # 检测验证码
    if code != check_code:
      return JsonResponse({'error': "验证码错误"},safe=False)

    # 手机号是否注册过
    same_account = models.Account.objects.filter(account_tel=tel)
    if same_account:
      return JsonResponse({'error': "手机号已被注册"},safe=False)

    # 满足条件，创建新用户
    dic = {
      'account_tel': tel,
      'password': hash_code("123456"),
      'add_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    models.Account.objects.create(**dic)

    return JsonResponse({'info': "注册成功，初始密码为123456"},safe=False)

  return JsonResponse({'error': "注册请求失败"},safe=False)



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