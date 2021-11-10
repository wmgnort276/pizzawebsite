from django.db import models

# Create your models here.
class Topping(models.Model):
    cost = models.IntegerField()
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
    name = models.CharField(max_length=100, blank=False)
    # class Size(models.TextChoices):
    SMALL='S'
    MEAN='M'
    BIG='L'
    choice = [(SMALL,'S'),(MEAN,'M'),(BIG,'L')]
    size = models.CharField(max_length=1,choices=choice,default='S')
    cost = models.IntegerField()
    image=models.ImageField(default='defaultpizza.webp',upload_to='pizza')
    def addtopping(self, topping_id):
        topping = Topping.objects.get(pk=topping_id)
        self.toppings.add(topping)
    def removetopping(self, topping_id):
        topping = Topping.objects.get(pk=topping_id)
        self.toppings.remove(topping)
    def __str__(self):
        return self.name
# class ToppingAmount(models.Model):
#     REGULAR = 1
#     DOUBLE = 2
#     TRIPLE = 3
#     AMOUNT_CHOICES = (
#         (REGULAR, 'Regular'),
#         (DOUBLE, 'Double'),
#         (TRIPLE, 'Triple'),
#     )
#     pizza = models.ForeignKey('Pizza', related_name='topping_amounts', on_delete=models.SET_NULL, null=True)
#     topping = models.ForeignKey('Topping', related_name='topping_amounts', on_delete=models.SET_NULL, null=True, blank=True)
#     amount = models.IntegerField(choices=AMOUNT_CHOICES, default=REGULAR)
class SideDishes(models.Model):
    name=models.CharField(max_length=100)
    cost = models.IntegerField()
    image=models.ImageField(default='defaultdishes.jpg', upload_to='sidedishes')
    def __str__(self):
        return self.name
class Combo(models.Model):
    name=models.CharField(max_length=100)
    cost = models.IntegerField()
    time = models.DateTimeField("Expires on")
    image = models.ImageField()
    numberperson = models.IntegerField()
    pizzas= models.ManyToManyField(Pizza)
    dishes = models.ManyToManyField(SideDishes)
    def __str__(self):
        return self.name
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
