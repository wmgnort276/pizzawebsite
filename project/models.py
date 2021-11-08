from django.db import models
import os,django
# Create your models here.
class Topping(models.Model):
    cost = models.IntegerField(max_length=6)
    name=models.CharField(max_length=100)
class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
    name = models.CharField(max_length=100, blank=False)
    class Size(models.TextChoice):
        SMALL='S'
        MEAN='M'
        BIG='L'
    size = models.CharField(max_length=1,choices=Size,default='S')
    # def addtopping(self, topping_id):
    #     topping = Topping.objects.get(pk=topping_id)
    #     self.toppings.add(topping)
    # def removetopping(self, topping_id):
    #     topping = Topping.objects.get(pk=topping_id):
    #     self.toppings.remove(topping)
    cost = models.IntegerField(max_length=6)
    image=models.ImageField(default='defaultpizza.webp', upload_to='pizza')
    def addtopping(self, topping_id):
        topping = Topping.objects.get(pk=topping_id)
        self.toppings.add(topping)
    def removetopping(self, topping_id):
        topping = Topping.objects.get(pk=topping_id):
        self.toppings.remove(topping)
class SideDishes(models.Model):
    name=models.CharField(max_length=100)
    cost = models.IntegerField(max_length=6)
    image=models.ImageField(default='defaultdishes', upload_to='sidedishes')
class Combo(models.Model):
    name=models.CharField(max_length=100)
    cost = models.IntegerField(max_length=6)
    time = models.DateTimeField("Expires on")
    image = models.ImageField()
    numberperson = models.IntegerField(max_length=1)
    pizzas= models.ManyToManyField(Pizza)
    dishes = models.ManyToManyField(SideDishes)
    def addpizza(self, pizza_id):
        pizza=Pizza.objects.get(pk=pizza_id)
        self.pizzas.add(pizza)
    def removepizza(self, pizza_id):
        pizza = Pizza.objects.get(pk=pizza_id)
        self.pizzas.add(pizza)
    def adddishes(self,dishes_id):
        dishes = SideDishes.objects.get(pk=dishes_id)
        self.dishes.add(dishes)
    def remvedishes(self, dishes_id):
        dishes = SideDishes.objects.get(pk=dishes_id)
        self.dishes.remove(dishes)