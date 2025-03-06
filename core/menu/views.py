from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, DeleteView
from menu.models import Item, Category, Order, OrderItem
from accounts.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from django.http import HttpResponseForbidden


class MenuListView(ListView):
    template_name = 'menu/menu.html'

    def get_queryset(self):
        items = Item.objects.filter(is_available=True).order_by('-id')
        return items
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
    context_object_name = 'items' 






class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'menu/order.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(phone_number=self.request.user)




class OrderAddView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        item_id = self.kwargs.get('id')  
        item = get_object_or_404(Item, id=item_id)

        order, created = Order.objects.get_or_create(phone_number=request.user)

        order_item, created = OrderItem.objects.get_or_create(order=order, item=item)

        if not created:
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(item)

        return redirect('menu:order-list')



class MenuDeleteView(LoginRequiredMixin, DeleteView):
    pass




class IncreaseOrderItemView(LoginRequiredMixin, View):
    def post(self, request, id, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, pk=id)

        if order_item.order.phone_number != request.user:
            return HttpResponseForbidden("You are not allowed to modify this item.")

        order_item.quantity += 1
        order_item.save()
        return redirect('menu:order-list')

class DecreaseOrderItemView(LoginRequiredMixin, View):
    def post(self, request, id, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, pk=id)

        if order_item.order.phone_number != request.user:
            return HttpResponseForbidden("You are not allowed to modify this item.")

        if order_item.quantity > 1:
            order_item.quantity -= 1
            order_item.save()
        else:
            order_item.delete() 

        return redirect('menu:order-list')