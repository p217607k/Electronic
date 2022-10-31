from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Images)
class ImageTub(admin.TabularInline):
    model= Images
class tagtub(admin.TabularInline):
    model= tag
class producttub(admin.ModelAdmin):
    inlines= [ImageTub,tagtub]

admin.site.register(tag)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Filter_price)
admin.site.register(Color)
class OderitemTub(admin.TabularInline):
    model= OrderItem
class Ordertub(admin.ModelAdmin):
    inlines = [OderitemTub]
    list_display=['first_name','email','phone','payment_id','paid','datetime']
    search_fields=['first_name','email','phone']
    list_editable = ['email','phone']
admin.site.register(Order,Ordertub)
admin.site.register(OrderItem)


admin.site.register(contect_us)

admin.site.register(Product,producttub)



