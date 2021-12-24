import re
from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg
from django.db.models.fields.mixins import NOT_PROVIDED
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm, fields
from datetime import date, datetime
from django.utils import timezone
from project.models import *

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image =models.ImageField(default="default.jpg",upload_to="profile_pictures")
    name = models.CharField(max_length=100,default='')
    number_phone = models.CharField(max_length=10,blank=False)
    address = models.CharField(max_length=500, blank=False)
    pub_date = models.DateField('Birthday',default=date.today)
    def __str__(self) :
        return f'{self.user.username}\'s Profile...'
    @receiver(post_save,sender=User)
    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['image','name','number_phone','address','pub_date']
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username}\''
    # @property
    def pricecart(self):
        price = 0
        order_set = Order.objects.filter(cart__id=self.id)
        for order in order_set:
            price +=order.price()
        return price
    def delived(self):
        a = Order.objects.filter(cart__id=self.id)
        return a.filter(delive="False")
    def notdelived(self):
        a = Order.objects.filter(cart__id=self.id)
        return a.filter(delive="True")
    @receiver(post_save,sender=User)
    def create_cart(sender,instance,created,**kwargs):
        if created:
            Cart.objects.create(user=instance)
    # def pricecart(self):
    #     price=int(0)
    #     order_set = Order.objects.filter(cart__id=self.id)
    #     for order in order_set:
    #         price +=order.cost()
    #     return price
class Order(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart', on_delete=models.SET_NULL,null=True, blank=True)
    name = models.CharField(max_length=100, blank=False)
    phonenumber = models.CharField(max_length=10,blank=False)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100)
    delive = models.BooleanField(default=False)
    create = models.DateTimeField(default = datetime.now())
    def __str__(self):
        return self.name +str(self.id)
    def price(self):
        cost = 0
        a = OrderSideDishes.objects.filter(order__id = self.id)
        for piza in a:
            cost +=piza.cost()
        b = OrderSideDishes.objects.filter(order__id = self.id)
        for side in b:
            cost+=side.cost()
        c = OrderCombo.objects.filter(order__id = self.id)
        for combo in c:
            cost+=combo.cost()
        return cost
    @property
    def cost(self):
        cost = 0
        a = OrderSideDishes.objects.filter(order__id = self.id)
        for piza in a:
            cost +=piza.cost()
        b = OrderSideDishes.objects.filter(order__id = self.id)
        for side in b:
            cost+=side.cost()
        c = OrderCombo.objects.filter(order__id = self.id)
        for combo in c:
            cost+=combo.cost()
        return cost
class OrderPizza(models.Model):
    order = models.ForeignKey(Order,related_name='orderpizza',on_delete= models.CASCADE, null = False)
    pizaa = models.ForeignKey(Pizza,related_name='pizaa', on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    def cost(self):
        return self.pizaa.cost*self.amount
    @property
    def pizza(self):
        return Pizza.objects.get(id = self.pizaa.id)
class OrderSideDishes(models.Model):
    order = models.ForeignKey(Order, related_name = 'orderside', on_delete = models.CASCADE)
    sidess = models.ForeignKey(SideDishes,related_name= 'sidess', on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    def cost(self):
        return self.sidess.cost*self.amount
    @property
    def sidedishes(self):
        return SideDishes.objects.get(id = self.sidess.id)
class OrderCombo(models.Model):
    order = models.ForeignKey(Order, related_name = 'ordercombo', on_delete = models.CASCADE)
    combobox = models.ForeignKey(Combo,related_name= 'combobox',on_delete = models.CASCADE)
    amount = models.IntegerField(default=1)
    def cost(self):
        return self.combobox.pricecombo()*self.amount
    @property
    def comboboss(self):
        return Combo.objects.get(id = self.combobox.id)
    
    