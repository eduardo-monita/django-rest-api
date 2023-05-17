from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^webhook/$', views.SimpleWebhook.as_view(), name='simple-webhook'),
    url(r'^lote/$', views.LoteListCreate.as_view(), name='lote-list-create'),
    url(r'^lote/(?P<pk>[0-9]+)/$', views.LoteDetail.as_view(), name='lote-detail'),
    url(r'^item-relat/$', views.ItemList.as_view(), name='item-list'),
    url(r'^item/$', views.ItemListCreate.as_view(), name='item-list-create'),
    url(r'^item/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view(), name='item-detail'),
    url(r'^cliente/$', views.ClienteListCreate.as_view(), name='cliente-list-create'),
    url(r'^cliente/(?P<pk>[0-9]+)/$', views.ClienteDetail.as_view(), name='cliente-detail'),
    url(r'^vendedor/$', views.VendedorList.as_view(), name='vendedor-list-create'),
    url(r'^pedido-relat/$', views.PedidoList.as_view(), name='pedido-list'),
    url(r'^pedido/$', views.PedidoListCreate.as_view(), name='pedido-list-create'),
    url(r'^pedido/(?P<pk>[0-9]+)/$', views.PedidoDetail.as_view(), name='item-detail'),
    url(r'^relatorio/$', views.PedidoRelatorio.as_view(), name='relatorio'),
]
