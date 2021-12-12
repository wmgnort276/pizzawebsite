from codecs import lookup
from django.db.models import fields, query
from rest_framework import serializers
from project.models import *
import project.views
class ToppingSerializers(serializers.Serializer):
    pk = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 100)
    cost = serializers.IntegerField()
    description = serializers.CharField(max_length = 200)
    # class Meta:
    #     model = Topping
    #     fields=('name','cost','countPizza')
    def create(self, validated_data):
        return Topping.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cost = validated_data.get('cost',instance.cost)
        instance.description = validated_data.get('countPizza', instance.description)
        instance.save()
        return instance
class SideDishesSerializers(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 100)
    cost = serializers.IntegerField()
    image = serializers.ImageField()
    description = serializers.CharField(max_length = 200)
    def create(self, validated_data):
        return SideDishes.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('image', instance)
        instance.save()
        return instance
class PizzaSerializers(serializers.Serializer):
    pk = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 100)
    cost = serializers.IntegerField()
    image = serializers.ImageField()
    description = serializers.CharField(max_length = 200)
    def create(self, validated_data):
        return Pizza.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('image', instance)
        instance.save()
        # instance.addtopping(topping_set)
class ComboSerializers(serializers.Serializer):
    pk = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 100)
    cost = serializers.IntegerField()
    image = serializers.ImageField()
    description = serializers.CharField(max_length = 200)
    def create(self, validated_data):
        return Pizza.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('image', instance)
        instance.save()
# Hàm để trả ra thông tin của các đối tượng trong combo
# Code API mới

class ToppingSerializer(serializers.HyperlinkedModelSerializer):
    # topping_amounts = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='name')
    # pk = serializers.IntegerField(read_only=True)
    topping_amount = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name = 'toppingamount-detail')
    cost = serializers.IntegerField()
    name = serializers.CharField(max_length = 100)
    image = serializers.ImageField()
    description = serializers.CharField(max_length = 200)
    class Meta:
        model = Topping
        fields = (
            'url',
            'cost',
            'name',
            'image',
            'description',
            # 'topping_amounts',
            'pk',
            'topping_amount'
        )
class ToppingAmountSerializer(serializers.HyperlinkedModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    pizza = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='name')
    topping = serializers.SlugRelatedField(queryset = Topping.objects.all(), slug_field='name')
    amount = serializers.ChoiceField(choices = ToppingAmount.AMOUNT_CHOICES)
    class Meta:
        model = ToppingAmount
        fields = ('url',
        'pk',
        'pizza',
        'topping',
        'amount',
        )
class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # topping_amounts = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='toppingamount-detail')
    pizza = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='comboamount-detail')
    topping_amounts = ToppingAmountSerializer(many = True)
    name = serializers.CharField(max_length = 100)
    cost = serializers.IntegerField()
    image = serializers.ImageField()
    description = serializers.CharField(max_length = 200)
    menu = serializers.ChoiceField(choices = Pizza.choi, read_only = True)
    score_fields = serializers.FloatField(source = 'score')
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
# class PizzaSerializer(serializers.HyperlinkedModelSerializer):
#     name = serializers.CharField(max_length = 100)
#     cost = serializers.IntegerField()
#     image = serializers.ImageField()
#     description = serializers.CharField(max_length = 200)
#     class Meta:
#         model = SideDishes
#         fields = (
#             'url',
#             'cost',
#             'name',
#             'image',
#             'description',
#         )
class ComboAmountSerializer(serializers.ModelSerializer):
    combo = serializers.SlugRelatedField(queryset = Combo.objects.all(), slug_field='name')
    pizza = PizzaSerializer(read_only = True)
    #pizza = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='name')
    # pk = serializers.IntegerField(read_only=True)
    size = serializers.ChoiceField(choices=ComboAmount.SIZE_CHOICES)
    amountPizza = serializers.IntegerField()
    #dishes = serializers.SlugRelatedField(queryset = SideDishes.objects.all(), slug_field='name')
    dishes = SideDishesSerializer(read_only = True)
    # dishes = SideDishesSerializers()
    amount = serializers.IntegerField()
    class Meta:
        model = ComboAmount
        fields = ('url',
            'combo',
            'pizza',
            'pk',
            'size',
            'amountPizza',
            'dishes',
            'amount',)
class ComboSerializer(serializers.HyperlinkedModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # combo = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='comboamount-detail')
    combocategory = serializers.SlugRelatedField(queryset = ComboCategory.objects.all(), slug_field='name')
    pizzas = PizzaSerializer(many=True)
    # sides = SideDishesSerializer(many = True)
    sides = SideDishesSerializer(many = True)
    combo = ComboAmountSerializer(many = True, read_only = True)
    name = serializers.CharField(max_length = 100)
    numberperson = serializers.IntegerField()
    time = serializers.DateTimeField()
    cost = serializers.IntegerField()
    image = serializers.ImageField()
    description = serializers.CharField(max_length = 200)
    menu = serializers.ChoiceField(choices=Pizza.choi, read_only = True)
    current_sides_fields = SideDishesSerializer(many = True, source = 'current_sides',read_only = True)
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
            'combo',
            'pizzas',
            'sides',
            'combocategory',
            'current_sides_fields',
            'score_fields',
            # 'side'
            # 'typeside'
            )
    # def __init__(self, *args, **kwargs):
    #     context = kwargs.pop("sides")
    #     self.combo_id = context.get('combo_id')
    #     super(ComboSerializer, self).__init__(*args, **kwargs)
    # def get_typeside(self,combo):
    #     # data = combo.sides
    #     return SideDishesSerializer(many = True, source = 'current_sides').data
class ComboCategorySerializer(serializers.HyperlinkedModelSerializer):
    category = ComboSerializer(many = True,read_only = True)
    class Meta:
        model = ComboCategory
        fields=(
            'url',
            'name',
            'image',
            'description',
            'category'
        )
class ScorePizzaSerialize(serializers.HyperlinkedModelSerializer):
    pizza = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='name')
    score = serializers.ChoiceField(choices=ScorePizza.SCORE_CHOICE)
    class Meta:
        model = ScorePizza
        fields = (
            'url',
            'pizza',
            'score'
        )
class ScoreSideSerializer(serializers.HyperlinkedModelSerializer):
    side = serializers.SlugRelatedField(queryset = SideDishes.objects.all(), slug_field = 'name')
    score = serializers.ChoiceField(choices = ScorePizza.SCORE_CHOICE)
    class Meta:
        model = ScoreSide
        fields = (
            'url',
            'side',
            'score'
        )
class ScoreComboSerializer(serializers.HyperlinkedModelSerializer):
    combo = serializers.SlugRelatedField(queryset = Combo.objects.all(), slug_field = 'name')
    score = serializers.ChoiceField(choices = ScorePizza.SCORE_CHOICE)
    class Meta:
        model = ScoreCombo
        fields = (
            'url',
            'combo',
            'score'
        )