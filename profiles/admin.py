from django.contrib import admin
from .models import *
# Register your models here.
class OrderPizzaInLine(admin.StackedInline):
    model = OrderPizza
    extra = 0
class OrderSideInLine(admin.StackedInline):
    model = OrderSideDishes
    extra = 0
class OrderComboInLine(admin.StackedInline):
    model = OrderCombo
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    fields_set = (
        (None, {
            'fields': ['name']
        }),
    )
    inlines = [OrderPizzaInLine,OrderSideInLine,OrderComboInLine]
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(Order,OrderAdmin)