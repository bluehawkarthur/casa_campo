from django.conf.urls import url
from .views import Inicio, Index, Main, LoginView, LogoutView


urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^inicio/$', Inicio.as_view(), name='inicio'),
    url(r'^main/$', Main.as_view(), name='main'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),


]