from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Pizza,PizzaAdmin)
class AmountToppingInLine(admin.StackedInline):
    model=ToppingAmount
    extra=0
class ComboAmountInLine(admin.StackedInline):
    model=ComboAmount
    extra = 1
class PizzaAdmin(admin.ModelAdmin):
    list_display=('name','cost')
    list_filter=['cost','toppings']
    search_fields=['name']
    fieldsets = (
        (None, {
            "fields": (
                ['name']
            ),
        }),
        (None,{
            'fields':['size']
        }),
        (None,{
            "fields":['cost']
        }),
        (None,{
            "fields":['image']
        }),
        (None,{
            "fields":['description']
        }
        ),
        (None,{
            'fields':['menu']
        }),
    )
    inlines = [AmountToppingInLine]
    exclude=('toppings',)
class ComboAdmin(admin.ModelAdmin):
    list_display=('name','numberperson','cost','time')
    list_filter=['numberperson','cost']
    search_fields=['name']
    fieldsets = (
        (None,{
            'fields':(
                ['combocategory']
            ),
        }
        ),
        (None, {
            "fields": (
                ['name']
            ),
        }),
        (None,{
            'fields':
            ['cost']
        }),
        (None,{
            'fields':['time']
        }),
        (None,{
            'fields':['image']
        }),
        (None,{
            'fields':['numberperson']
        }),
        (None,{
            "fields":['description']
        }
        ),
         (None,{
            'fields':['menu']
        }),
        (None, {
            "fields": (
                ['pizzas']
            ),
        }),
        (None, {
            "fields": (
                ['sides']
            ),
        }),
    )
    inlines=[ComboAmountInLine]
    # exclude=['pizzas','dishes',]
class ToppingAdmin(admin.ModelAdmin):
    list_display=('name','cost')
    list_filter=['cost']
    search_fields=['name']
class SideDishesAdmin(admin.ModelAdmin):
    list_display=('name','cost')
    list_filter=['cost']
    search_fields=['name']
class ComboAmountAdmin(admin.ModelAdmin):
    list_filter=['combo']
    list_display=('combo','pizza','size','amountPizza','dishes','amount')
class ToppingAmountAdmin(admin.ModelAdmin):
    list_filter=['pizza']
    list_display=('pizza','topping','amount')
    
admin.site.register(Topping,ToppingAdmin)
admin.site.register(SideDishes,SideDishesAdmin)
admin.site.register(Pizza,PizzaAdmin)
admin.site.register(Combo,ComboAdmin)
admin.site.register(ToppingAmount, ToppingAmountAdmin)
admin.site.register(ComboAmount,ComboAmountAdmin)
admin.site.register(ComboCategory)
