# from django.db.models import query
# from django.db.models.fields import IntegerField
# from myproject.project.serializers import ComboSerializers
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from .models import *
from project.models import *
from django.contrib.auth.models import User
# from project.serializers import *
# from project.serializers import ComboSerializer
class ProfilesSerializaer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset = User.objects.all(),slug_field='username')
    image =serializers.ImageField()
    name = serializers.CharField(max_length=100)
    number_phone = serializers.CharField(max_length=10)
    address = serializers.CharField(max_length=500)
    pub_date = models.DateField()
    class Meta:
        model = Profile
        fields=(
            'url',
            'image',
            'name',
            'number_phone',
            'address',
            'pub_date',
            'user',
            # 'cost',
        )
class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # topping_amounts = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='toppingamount-detail')
    pizza = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='comboamount-detail')
    # topping_amounts = ToppingAmountSerializer(many = True)
    name = serializers.CharField(max_length = 100, read_only = True)
    cost = serializers.IntegerField(read_only = True)
    image = serializers.ImageField(read_only = True)
    description = serializers.CharField(max_length = 200, read_only = True)
    menu = serializers.ChoiceField(choices = Pizza.choi, read_only = True)
    score_fields = serializers.FloatField(source = 'score', read_only = True)
    class Meta:
        model = Pizza
        fields = (
            'url',
            'cost',
            'name',
            'size',
            'pk',
            'image',
            'description',
            'menu',
            'topping_amounts',
            'pizza',
            'score_fields'
        )
class SideDishesSerializer(serializers.HyperlinkedModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    dishes = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='comboamount-detail')
    name = serializers.CharField(max_length = 100)
    cost = serializers.IntegerField()
    image = serializers.ImageField()
    description = serializers.CharField(max_length = 200)
    type = serializers.ChoiceField(choices= SideDishes.TYPE_CHOICES)
    menu = serializers.ChoiceField(choices = Pizza.choi)
    score_fields = serializers.FloatField(source = 'score')
    class Meta:
        model = SideDishes
        fields = (
            'url',
            'name',
            'pk',
            'cost',
            'image',
            'description',
            'type',
            'menu',
            # 'test',
            'dishes',
            'score_fields',
        )
# class ComboAmountSerializer(serializers.ModelSerializer):
#     combo = serializers.SlugRelatedField(queryset = Combo.objects.all(), slug_field='name')
#     pizza = PizzaSerializer()
#     #pizza = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='name')
#     # pk = serializers.IntegerField(read_only=True)
#     size = serializers.ChoiceField(choices=ComboAmount.SIZE_CHOICES)
#     amountPizza = serializers.IntegerField()
#     #dishes = serializers.SlugRelatedField(queryset = SideDishes.objects.all(), slug_field='name')
#     dishes = SideDishesSerializer(read_only = True)
#     # dishes = SideDishesSerializers()
#     amount = serializers.IntegerField()
#     class Meta:
#         model = ComboAmount
#         fields = ('url',
#             'combo',
#             'pizza',
#             'pk',
#             'size',
#             'amountPizza',
#             'dishes',
#             'amount',)
class PizzaInComboSerializer(serializers.HyperlinkedModelSerializer):
    combo = serializers.SlugRelatedField(queryset = Combo.objects.all(), slug_field='name')
    pizzacombo = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='pk')
    pizza = PizzaSerializer(read_only = True, source = 'piza')
    class Meta:
        model = PizzaInCombo
        fields = (
            'url',
            'pk',
            'combo',
            'pizzacombo',
            'pizza',
            # 'amount',
        )
class SideDishesInComboSerializer(serializers.HyperlinkedModelSerializer):
    combo = serializers.SlugRelatedField(queryset = Combo.objects.all(), slug_field='name')
    sidecombo = serializers.SlugRelatedField(queryset = SideDishes.objects.all(), slug_field='pk')
    sidedishes = SideDishesSerializer(read_only = True, source = 'side')
    type = serializers.ChoiceField(choices=SideDishes.TYPE_CHOICES, read_only = True)
    sides = SideDishesSerializer(read_only = True, source = 'sidedishes', many=True)
    class Meta:
        model = SideDishesInCombo
        fields = (
            'url',
            'combo',
            'pk',
            'sidecombo',
            'sidedishes',
            'type',
            'sides',
            # 'amount',
        )
class ComboSerializer(serializers.HyperlinkedModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # combo = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='comboamount-detail')
    # combocategory = serializers.SlugRelatedField(queryset = ComboCategory.objects.all(), slug_field='name')
    pizzaincombo = PizzaInComboSerializer(many = True)
    sideincombo = SideDishesInComboSerializer(many = True)
    pizzas = PizzaSerializer(many=True, read_only = True)
    # sides = SideDishesSerializer(many = True)
    # sides = SideDishesSerializer(many = True)
    # combo = ComboAmountSerializer(many = True, read_only = True)
    name = serializers.CharField(max_length = 100)
    numberperson = serializers.IntegerField()
    time = serializers.DateTimeField()
    cost = serializers.IntegerField()
    image = serializers.ImageField()
    description = serializers.CharField(max_length = 200)
    menu = serializers.ChoiceField(choices=Pizza.choi, read_only = True)
    current_sides_fields = SideDishesSerializer(many = True, source = 'current_sides',read_only = True)
    price_field = serializers.IntegerField(source = 'price', read_only = True)
    score_fields = serializers.FloatField(source = 'score', read_only = True)
    class Meta:
        model = Combo
        fields = ('url',
            'name',
            'time',
            'pk',
            'numberperson',
            'cost',
            'image',
            'percent',
            'description',
            'menu',
            # 'combo',
            'pizzaincombo',
            'sideincombo',
            'pizzas',
            # 'sides',
            # 'combocategory',
            'price_field',
            'current_sides_fields',
            'score_fields',
            # 'side'
            # 'typeside'
            )
class OrderPizzaSerializer(serializers.HyperlinkedModelSerializer):
    # order = serializers.StringRelatedField()
    order = serializers.SlugRelatedField(queryset = Order.objects.all(), slug_field='pk')
    # pizaa = PizzaSerializer()
    pizaa = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='pk')
    pizzaa = PizzaSerializer(source = 'pizza', read_only = True)
    #pizaa = serializers.PrimaryKeyRelatedField(queryset = Pizza.objects.all(),pk_field=UUIDField(format='hex'))
    # pizaa = serializers.HyperlinkedIdentityField(view_name='pizza-detail')
    cost  = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = OrderPizza
        fields = (
            'url',
            'pk',
            'order',
            'pizaa',
            'pizzaa',
            'amount',
            'cost'

        )
    def get_cost(self,orderpiza):
        return orderpiza.pizaa.cost*orderpiza.amount
class OrderSideSerializer(serializers.HyperlinkedModelSerializer):
    # order = serializers.StringRelatedField()

    sidess = serializers.SlugRelatedField(queryset = SideDishes.objects.all(), slug_field='pk')
    # sidess = serializers.HyperlinkedRelatedField(read_only = True, view_name='sidedishes-detail')
    sidedis = SideDishesSerializer(read_only = True, source = 'sidedishes')
    cost = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = OrderSideDishes
        fields = (
            'url',
            'pk',
            'order',
            'sidess',
            'sidedis',
            'amount',
            'cost'
        )
    def get_cost(self,orderside):
        return orderside.sidess.cost*orderside.amount
class OrderComboSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.StringRelatedField()
    combobox = serializers.SlugRelatedField(queryset = Combo.objects.all(), slug_field='pk')
    # combobox = serializers.HyperlinkedRelatedField(read_only = True, view_name='combo-detail')
    comboinformation = ComboSerializer(read_only = True, source = 'comboboss')
    cost = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = OrderCombo
        fields = (
            'url',
            'pk',
            'order',
            'combobox',
            'comboinformation',
            'amount',
            'cost'
        )
    def get_cost(self, ordercombo):
        return ordercombo.combobox.cost*ordercombo.amount
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    # cart = serializers.SlugRelatedField(queryset = Cart.objects.all(), slug_field='__str__')
    # cart = serializers.StringRelatedField()
    # piza = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='name')
    # side = serializers.SlugRelatedField(queryset = SideDishes.objects.all(), slug_field='name')
    # combobox = serializers.SlugRelatedField(queryset = Combo.objects.all(), slug_field = 'name')
    # combobox = serializers.HyperlinkedRelatedField(read_only = True, view_name = 'combo-detail')
    # cost_fields = models.IntegerField(source = 'cost')
    # cost  = serializers.SerializerMethodField(read_only=True)
    orderpizza = OrderPizzaSerializer(many = True)
    orderside = OrderSideSerializer(many = True)
    ordercombo = OrderComboSerializer( many = True)
    cost_fields = serializers.IntegerField(source = 'cost')
    class Meta:
        model = Order
        fields = (
            'url',
            'cart',
            'pk',
            # 'piza',
            # 'amountpizza',
            # 'side',
            # 'amountside',
            # 'combobox',
            # 'amountcombo',
            'name',
            'phonenumber',
            'email',
            'address',
            'orderpizza',
            'orderside',
            'ordercombo',
            'delive',
            'cost_fields'
        )
class CartSerializer(serializers.HyperlinkedModelSerializer):
    cart = OrderSerializer(many=True,read_only = True)
    name_fields = serializers.CharField(source = '__str__')
    pricecart_fields = serializers.IntegerField(source = 'pricecart')
    # cost = serializers.SerializerMethodField('get_cost')
    delived_fields = OrderSerializer(many = True, source = 'delived', read_only = True)
    notdelived_fields = OrderSerializer(many = True, source = 'notdelived', read_only = True)
    class Meta:
        model = Cart
        fields=(
            'url',
            'pk',
            'cart',
            'name_fields',
            # 'cost'
            'pricecart_fields',
            'delived_fields',
            'notdelived_fields',
        )
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # name = serializers.CharField(max_length = 50)
    class Meta:
        model = User
        fields=(
            'username',
            'first_name',
            # 'name',
            'password',
            # 'password2'
        )
# class ScorePizzaSerialize(serializers.HyperlinkedModelSerializer):
#     pizza = serializers.StringRelatedField()
#     score = serializers.ChoiceField(choices=ScorePizza.SCORE_CHOICE)
#     class Meta:
#         model = ScorePizza
#         fields = (
#             'url',
#             'pizza',
#             'score'
#         )