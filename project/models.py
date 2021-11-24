from django.db import models

# Create your models here.
class Topping(models.Model):
    cost = models.IntegerField()
    name=models.CharField(max_length=100)
    image = models.ImageField(default = 'topping.jpg', upload_to='topping')
    description = models.CharField(max_length = 200, blank = True)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
class Pizza(models.Model):
    # toppings = models.ManyToManyField(Topping)
    toppings = models.ManyToManyField('Topping', through='ToppingAmount', related_name='pizzas')
    name = models.CharField(max_length=100, blank=False)
    # class Size(models.TextChoices):
    SMALL='S'
    MEAN='M'
    BIG='L'
    choice = [(SMALL,'S'),(MEAN,'M'),(BIG,'L')]
    size = models.CharField(max_length=1,choices=choice,default='S')
    cost = models.IntegerField()
    image=models.ImageField(default='defaultpizza.webp',upload_to='pizza')
    description = models.CharField(max_length = 200, blank = True)
    class Meta:
        ordering = ('name',)
    def addtopping(self, topping_set):
        # topping = Topping.objects.get(pk=topping_id)
        for tp in topping_set:
            self.toppings.add(tp)
    def addtopping(self, topping_id):
        topping = Topping.objects.get(topping_id)
        self.toppings.add(topping)
    def removetopping(self, topping_id):
        topping = Topping.objects.get(pk=topping_id)
        self.toppings.remove(topping)
    def __str__(self):
        return self.name
class ComboAmount(models.Model):
    combo=models.ForeignKey('Combo',on_delete=models.SET_NULL, null=True,related_name='combo')
    # combo=models.ForeignKey('Pizza',on_delete=models.SET_NULL, null=True)
    pizza = models.ForeignKey('Pizza', on_delete=models.SET_NULL, null=True, blank=True,related_name='pizza')
    SMALL='S'
    MEAN='M'
    BIG='L'
    SIZE_CHOICES=(
        (SMALL,'S'),
        (MEAN,'M'),
        (BIG,'L')
    )
    size=models.CharField(max_length=1,choices=SIZE_CHOICES,default='S')
    amountPizza=models.IntegerField(default=1)
    # combodishes=models.ForeignKey('Combo','Pizza',on_delete=models.SET_NULL, null=True)
    dishes=models.ForeignKey('SideDishes', on_delete=models.SET_NULL, null=True, blank=True,related_name='dishes')
    amount = models.IntegerField(default=1)
    class Meta:
        ordering = ('combo','pizza','dishes',)
    def __str__(self):
        return self.combo.name
class ToppingAmount(models.Model):
    REGULAR = 1
    DOUBLE = 2
    TRIPLE = 3
    AMOUNT_CHOICES = (
        (REGULAR, 'Regular'),
        (DOUBLE, 'Double'),
        (TRIPLE, 'Triple'),
    )
    pizza = models.ForeignKey('Pizza', related_name='topping_amounts', on_delete=models.SET_NULL, null=True)
    # topping = models.ForeignKey('Topping', related_name='topping_amounts', on_delete=models.SET_NULL, null=True, blank=True)
    topping = models.ForeignKey('Topping', related_name='topping_amount', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField(choices=AMOUNT_CHOICES, default=REGULAR)
    def __str__(self):
        return self.pizza.name
class SideDishes(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    image = models.ImageField(default='defaultdishes.jpg', upload_to='sidedishes')
    description = models.CharField(max_length = 200, blank = True)
    def __str__(self):
        return self.name
class Combo(models.Model):
    name=models.CharField(max_length=100)
    cost = models.IntegerField()
    time = models.DateTimeField("Expires on")
    image = models.ImageField(default = 'combo', upload_to = 'combo')
    numberperson = models.IntegerField()
    description = models.CharField(max_length = 200, blank = True)
    pizzas= models.ManyToManyField(Pizza,through='ComboAmount')
    dishes = models.ManyToManyField(SideDishes,through='ComboAmount')
    class Meta:
        ordering = ('name',)
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
