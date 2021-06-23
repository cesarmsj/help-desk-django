from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/', home, name='home'),
    url(r'^user_logout/', user_logout, name='user_logout'),
    url(r'^atendente_login/', atendente_login, name='atendente_login'),
    url(r'^atendente_home/', atendente_home, name='atendente_home'),
    url(r'^atendente_list/', atendente_list, name='atendente_list'),
    url(r'^atendente_create/', atendente_create, name='atendente_create'),
#    url(r'^atendente_update/(?P<pk>[0-9]+)', atendente_update, name='atendente_update'),
    url(r'^atendente_delete/(?P<pk>[0-9]+)', atendente_delete, name='atendente_delete'),
    url(r'^cliente_login/', cliente_login, name='cliente_login'),
    url(r'^cliente_home/', cliente_home, name='cliente_home'),
    url(r'^cliente_list/', cliente_list, name='cliente_list'),
    url(r'^cliente_create/', cliente_create, name='cliente_create'),
#    url(r'^cliente_update/(?P<pk>[0-9]+)', cliente_update, name='cliente_update'),
    url(r'^cliente_delete/(?P<pk>[0-9]+)', cliente_delete, name='cliente_delete'),
    url(r'^chamado_create/(?P<pk>[0-9]+)', chamado_create, name='chamado_create'),
    url(r'^chamado_list/(?P<pk>[0-9]+)', chamado_create, name='chamado_list'),
]