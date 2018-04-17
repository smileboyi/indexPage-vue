from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
  # url(r'login$', views.login),
  # url(r'logout$', views.logout),
  # url(r'register$', views.register),
  url(r'gift_list$', views.gift_list),
  url(r'hr_list$', views.hr_list),
]