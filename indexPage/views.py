from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt
from indexPage.utils import check_code, token
import datetime
from . import models
import json
import io

# Create your views here.


# 转成哈希值
def hash_code(ps, salt='webapp'):
  # 如果不加盐，为None时，那么每次生成的哈希都不一样
  return make_password(ps, salt, 'pbkdf2_sha256')


# ps处理后比较原哈希值
def check_hash(ps, hash_code):
  return check_password(ps, hash_code)


# 验证码图片
def create_code_img(request):
  # 直接在内存开辟一点空间存放临时生成的图片
  f = io.BytesIO()
  # 调用check_code生成照片和验证码
  img, code = check_code.create_validate_code()
  # 将验证码存在服务器的session中，用于校验
  request.session['check_code'] = code 
  # 生成的图片放置于开辟的内存中
  img.save(f,'PNG')
  # 将内存的数据读取出来，并以HttpResponse返回
  return HttpResponse(f.getvalue(), 'image/png')



# 用户注册
@csrf_exempt
@require_http_methods(["POST"])
def register(request):
  if request.method == "POST":
    # 获取用户数据
    tel = request.POST.get('tel', None)
    code = request.POST.get('code', None)
    check_code = ''
    try:
      check_code = request.session['check_code']
    except:
      return JsonResponse({'error': "请输入验证码"},safe=False)

    # 如果是脚本模拟登录的话（跳过浏览器的验证），需要做None判断，否则code.lower()会报错
    if not tel and not code:
      return JsonResponse({'error': "请填写信息"},safe=False)

    # 检测验证码
    if code.lower() != check_code.lower():
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



# 用户登录
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
  tel = request.POST.get('tel', None)
  password = request.POST.get('password', None)
  message = "登录请求失败"

  # 验证用户
  if tel and password:
    try:
      account = models.Account.objects.get(account_tel = tel)
      # 用户密码是否正确
      if check_hash(password,hash_code(password)):
        # 登录成功设置会话，还可以设置cookie
        message = "欢迎回来"
        request.session['is_login'] = True
        request.session['account_tel'] = tel
        _token = token.token_confirm.generate_validate_token(tel)
        request.session['session_token'] = _token

        return JsonResponse({'info': message,"token": _token},safe=False)
      else:
        # 也有可能输错了手机号，但密码输对了
        message = "手机号或密码有误！"
    except:
      message = "用户不存在，请先注册！"

  # 登录失败，附上错误提示信息
  return JsonResponse({'error': message},safe=False)


# 用户注销
@csrf_exempt
@require_http_methods(["POST"])
def logout(request):
  # 清空数据
  try:
    _token = request.session['session_token']
    token.token_confirm.remove_validate_token(_token)
    request.session.flush()
  except:
    pass
  finally:
    return JsonResponse({'info': '账户已注销'},safe=False)



# 获取礼品列表
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



# 获取hr列表
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