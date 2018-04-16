from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.


def hash_code(s, salt='mysite'):
  h = hashlib.sha256()  # sha256算法
  s += salt             # 加点盐
  h.update(s.encode())  # update方法只接收bytes类型
  return h.hexdigest()


def index(request):
  return render(request, 'login/index.html')