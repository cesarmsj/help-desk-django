from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('user_logout/', user_logout, name='user_logout'),
    path('atendente_login/', atendente_login, name='atendente_login'),
    path('atendente_home/', atendente_home, name='atendente_home'),
#    path('atendente_list/', atendente_list, name='atendente_list'),
    path('atendente_create/', atendente_create, name='atendente_create'),
#    url(r'^atendente_update/(?P<pk>[0-9]+)', atendente_update, name='atendente_update'),
#    path('atendente_delete/<str:pk>/', atendente_delete, name='atendente_delete'),
    path('cliente_login/', cliente_login, name='cliente_login'),
    path('cliente_home/', cliente_home, name='cliente_home'),
#    path('cliente_list/', cliente_list, name='cliente_list'),
    path('cliente_create/', cliente_create, name='cliente_create'),
#    url(r'^cliente_update/(?P<pk>[0-9]+)', cliente_update, name='cliente_update'),
#    path('cliente_delete/<str:pk>/', cliente_delete, name='cliente_delete'),
    path('chamado_create/<str:pk>/', chamado_create, name='chamado_create'),
    re_path('chamado_list/(?P<filter>\w+)/$', chamado_list, name='chamado_list'),
    path('chamado_interacao_list/<str:chamado>/', chamado_interacao_list, name='chamado_interacao_list'),
    path('chamado_interacao_create/<str:id_chamado>/', chamado_interacao_create, name='chamado_interacao_create'),
]