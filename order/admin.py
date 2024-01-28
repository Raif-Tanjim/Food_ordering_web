import datetime
from django.urls import reverse
from django.contrib import admin
from .models import Order, OrderItem

def order_name(obj):
    return '%s %s' % (obj.first_name, obj.last_name)

order_name.short_description = 'Name'
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    
    
def admin_order_shipped(modelAdmin, request, queryset):
    for order in queryset:
        order.shipped_date =datetime.datetime.now()
        order.status = Order.SHIPPED
        order.save()
    return 
admin_order_shipped.short_description ='Set shipped' 
   
def admin_order_delivered(modelAdmin, request, queryset):
    for order in queryset:
        order.delivered_date =datetime.datetime.now()
        order.status = Order.DELIVERED
        order.save()
    return 
admin_order_delivered.short_description ='Set delivered' 

class OrderAdmin(admin.ModelAdmin):
    
    def serial_number(self, obj):
        queryset = Order.objects.filter(created_at__lte=obj.created_at).order_by('created_at')
        return queryset.count()
    
    def get_queryset(self, request):
        # Override get_queryset to order by created_at
        return super().get_queryset(request).order_by('created_at')

    list_display = ['serial_number','order_id', order_name, 'status',  'created_at']
    list_filter = ['created_at','status']
    search_fields = ['first_name','address']
    inlines = [OrderItemInline]
    actions = [admin_order_shipped, admin_order_delivered]
    
    
    
    

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
