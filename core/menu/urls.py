from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.MenuListView.as_view(), name='menu-list'),
    path('order/', views.OrderListView.as_view(), name='order-list'),
    path('order/add/<int:id>/', views.OrderAddView.as_view(), name='order-add'),
    path('orders/increase/<int:id>/', views.IncreaseOrderItemView.as_view(), name='increase'),
    path('orders/decrease/<int:id>/', views.DecreaseOrderItemView.as_view(), name='decrease'),
    path('order/delete/', views.MenuDeleteView.as_view(), name='order-delete'),

]

