from django.db.models import query
from django.db.models.fields import IntegerField
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from .models import *
from project.models import *
from django.contrib.auth.models import User
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
# class OrderSerializer(serializers.HyperlinkedModelSerializer):
#     # cart = serializers.SlugRelatedField(queryset = Cart.objects.all(), slug_field='__str__')
#     # cart = serializers.StringRelatedField()
#     # piza = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='name')
#     # side = serializers.SlugRelatedField(queryset = SideDishes.objects.all(), slug_field='name')
#     # combobox = serializers.SlugRelatedField(queryset = Combo.objects.all(), slug_field = 'name')
#     # combobox = serializers.HyperlinkedRelatedField(read_only = True, view_name = 'combo-detail')
#     # cost_fields = models.IntegerField(source = 'cost')
#     # cost  = serializers.SerializerMethodField(read_only=True)
#     orderpizza = OrderPizzaSerializer(many = True)
#     orderside = OrderPizzaSerializer(many = True)
#     ordercombo = OrderComboSerializer( many = True)
#     class Meta:
#         model = Order
#         fields = (
#             'url',
#             'cart',
#             'pk',
#             # 'piza',
#             # 'amountpizza',
#             # 'side',
#             # 'amountside',
#             # 'combobox',
#             # 'amountcombo',
#             'orderpizza',
#             'orderside',
#             'ordercombo'
#             'delive',
#             # 'cost'
#         )
    # def get_cost(self,cart):
    #     return cart.piza.cost*cart.amountpizza + cart.side.cost*cart.amountside + cart.combobox.cost*cart.amountcombo
# class CartSerializer(serializers.HyperlinkedModelSerializer):
#     cart = OrderSerializer(many=True,read_only = True)
#     name_fields = serializers.CharField(source = '__str__')
#     pricecart_fields = serializers.IntegerField(source = 'pricecart')
#     # cost = serializers.SerializerMethodField('get_cost')
#     delived_fields = OrderSerializer(many = True, source = 'delived', read_only = True)
#     notdelived_fields = OrderSerializer(many = True, source = 'notdelived', read_only = True)
#     class Meta:
#         model = Cart
#         fields=(
#             'url',
#             'pk',
#             'cart',
#             'name_fields',
#             # 'cost'
#             'pricecart_fields',
#             'delived_fields',
#             'notdelived_fields',
#         )
    # def get_cost(self,carts):
    #     price = 0
    #     for order in carts.cart:
    #         price+=order.cost
    #     return price
class OrderPizzaSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.StringRelatedField()
   # pizaa = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='name')
    pizaa = serializers.HyperlinkedRelatedField(read_only = True, view_name='pizza-detail')
    cost  = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = OrderPizza
        fields = (
            'url',
            'pk',
            'order',
            'pizaa',
            'amount',
            'cost'

        )
    def get_cost(self,orderpiza):
        return orderpiza.pizaa.cost*orderpiza.amount
class OrderSideSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.StringRelatedField()
    #sidess = serializers.SlugRelatedField(queryset = SideDishes.objects.all(), slug_field='name')
    sidess = serializers.HyperlinkedRelatedField(read_only = True, view_name='sidedishes-detail')
    cost = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = OrderSideDishes
        fields = (
            'url',
            'pk',
            'order',
            'sidess',
            'amount',
            'cost'
        )
    def get_cost(self,orderside):
        return orderside.sidess.cost*orderside.amount
class OrderComboSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.StringRelatedField()
   # combobox = serializers.SlugRelatedField(queryset = Combo.objects.all(), slug_field='name')
    combobox = serializers.HyperlinkedRelatedField(read_only = True, view_name='combo-detail')
    cost = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = OrderCombo
        fields = (
            'url',
            'pk',
            'order',
            'combobox',
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