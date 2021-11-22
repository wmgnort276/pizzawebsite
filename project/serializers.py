from django.db.models import fields, query
from rest_framework import serializers
from project.models import *
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
# class ComboAmountSerializer(serializers.ModelSerializer):
#     combo = serializers.SlugRelatedField(queryset = Combo.objects.all(), slug_field='name')
#     pizza = serializers.SlugRelatedField(queryset = Pizza.objects.all(), slug_field='name')
#     size = serializers.ChoiceField(choices=ComboAmount.SIZE_CHOICES)
#     amountPizza = serializers.IntegerField()
#     dishes = serializers.SlugRelatedField(queryset = SideDishes.objects.all(), slug_field='name')
#     amount = serializers.IntegerField()
#     class Meta:
#         model = ComboAmount
#         fields = ('url',
#             'combo',
#             'pizza',
#             'size',
#             'amountPizza',
#             'dishes',
#             'amount')
# class ComboSerializer(serializers.HyperlinkedModelSerializer):
#     comboamounts = ComboAmountSerializer(many = True, read_only = True)
#     name = serializers.CharField(max_length = 100)
#     cost = serializers.IntegerField()
#     image = serializers.ImageField()
#     description = serializers.CharField(max_length = 200)
#     class Meta:
#         model = Combo
#         fields = ('url',
#             'name',
#             'cost',
#             'image',
#             'description',
#             'comboamounts')
