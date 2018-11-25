from django.conf.urls import url
from . import views

urlpatterns = [
    url('$', views.login, name='login'),
    url('$', views.load_users_from_api, name='load_users_from_api'),
    url('$', views.get_user, name='get_user')
]
