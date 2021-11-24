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
    topping_amounts = ToppingAmountSerializer(many = True, read_only = True)
    name = serializers.CharField(max_length = 100)
    cost = serializers.IntegerField()
    image = serializers.ImageField()
    description = serializers.CharField(max_length = 200)
    class Meta:
        model = Pizza
        fields = (
            'url',
            'cost',
            'name',
            'pk',
            'image',
            'description',
            'topping_amounts',
            'pizza'
        )
class SideDishesSerializer(serializers.HyperlinkedModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    dishes = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name='comboamount-detail')
    name = serializers.CharField(max_length = 100)
    cost = serializers.IntegerField()
    image = serializers.ImageField()
    description = serializers.CharField(max_length = 200)
    class Meta:
        model = SideDishes
        fields = (
            'url',
            'name',
            'pk',
            'cost',
            'image',
            'description',
            'dishes'
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
    # pizza = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='name')
    pizza = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='name')
    # pk = serializers.IntegerField(read_only=True)
    size = serializers.ChoiceField(choices=ComboAmount.SIZE_CHOICES)
    amountPizza = serializers.IntegerField()
    dishes = serializers.SlugRelatedField(queryset = SideDishes.objects.all(), slug_field='name')
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
    combo = ComboAmountSerializer(many = True, read_only = True)
    name = serializers.CharField(max_length = 100)
    numberperson = serializers.IntegerField()
    time = serializers.DateTimeField()
    cost = serializers.IntegerField()
    image = serializers.ImageField()
    description = serializers.CharField(max_length = 200)
    class Meta:
        model = Combo
        fields = ('url',
            'name',
            'time',
            'pk',
            'numberperson',
            'cost',
            'image',
            'description',
            'combo')
