from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
  # url(r'login$', views.login),
  # url(r'logout$', views.logout),
  url(r'captcha$', views.create_code_img),
  url(r'register$', views.register),
  url(r'gift/list$', views.gift_list),
  url(r'hr/list$', views.hr_list),
]