# from re import S
from django.db.models.query_utils import check_rel_lookup_compatibility
from django.shortcuts import render
from rest_framework import filters
# from django_filters import AllValuesFilter
from django.http import HttpResponse
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response
from project.serializers import *
from project.models import *
from project.tests import * 
# Create your views here.
#Code API mới

class ToppingList(generics.ListCreateAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    name = 'topping-list'
class ToppingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
    name = 'topping-detail'
class ToppingAmountList(generics.ListCreateAPIView):
    queryset = ToppingAmount.objects.all()
    serializer_class = ToppingAmountSerializer
    name = 'toppingamount-list'
class ToppingAmountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToppingAmount.objects.all()
    serializer_class = ToppingAmountSerializer
    name = 'toppingamount-detail'
class ComboAmountList(generics.ListCreateAPIView):
    queryset = ComboAmount.objects.all()
    serializer_class = ComboAmountSerializer
    name = 'comboamount-list'
class ComboAmountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComboAmount.objects.all()
    serializer_class = ComboAmountSerializer
    name = 'comboamount-detail'
class ComboList(generics.ListCreateAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer
    name = 'combo-list'
class ComboDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer
    name = 'combo-detail'
    filter_fields = ['sides']
class PizzaList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    name = 'pizza-list'
    filter_fields = ['size']
class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    name = 'pizza-detail'
# class SideDishesFilter(filters.Fie):
#     sidedishes_type = AllValuesFilter(name = 'sidedishes_type')
#     class Meta:
#         model = SideDishes
#         fields =(
#             'sideshes_type',
#         )
class SideDishesList(generics.ListCreateAPIView):
    queryset = SideDishes.objects.all()
    serializer_class = SideDishesSerializer
    name = 'sidedishes-list'
    filter_fields = ['type','name']
class SideDishesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SideDishes.objects.all()
    serializer_class = SideDishesSerializer
    name = 'sidedishes-detail'
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['type']
#     filter_fields = (
#     'type',
#     )
#     search_fields = (
#     'type',
#     )
#     ordering_fields = (
#     'type',
#     )
class ScorePizzaList(generics.ListCreateAPIView):
    queryset = ScorePizza.objects.all()
    serializer_class = ScorePizzaSerialize
    name = 'scorepizza-list'
class ScorePizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScorePizza.objects.all()
    serializer_class = ScorePizzaSerialize
    name = 'scorepizza-detail'
class ScoreSideList(generics.ListCreateAPIView):
    queryset = ScoreSide.objects.all()
    serializer_class = ScoreSideSerializer
    name = 'scoreside-list'
class ScoreSideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScoreSide.objects.all()
    serializer_class = ScoreSideSerializer
    name = 'scoreside-detail'
class ScoreComboList(generics.ListCreateAPIView):
    queryset = ScoreCombo.objects.all()
    serializer_class = ScoreComboSerializer
    name = 'scorecombo-list'
class ScoreComboDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScoreCombo.objects.all()
    serializer_class = ScoreComboSerializer
    name = 'scorecombo-detail'
class ComboCategoryList(generics.ListCreateAPIView):
    queryset = ComboCategory.objects.all()
    serializer_class = ComboCategorySerializer
    name = 'combocategory-list'
class ComboCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComboCategory.objects.all()
    serializer_class = ComboCategorySerializer
    name = 'combocategory-detail'
class APIRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'pizzas': reverse(PizzaList.name, request=request),
            'toppings': reverse(ToppingList.name, request=request),
            'toppingamounts': reverse(ToppingAmountList.name, request=request),
            'combos': reverse(ComboList.name, request = request),
            'comboamounts': reverse(ComboAmountList.name, request = request),
            'sidedishes': reverse(SideDishesList.name , request=request),
            'combocategorys': reverse(ComboCategoryList.name,request=request),
        })
# class SideDishesFilter(filters.FilterSet):
#     sidedishes_type = AllValuesFilter(name = 'sidedishes_type')
#     class Meta:
#         model = SideDishes
#         fields =(
#             'sideshes_type',
#         )
# Code API cũ


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data) 
        kwargs['content_type'] = 'application/json'
        # kwargs['content_type'] = "multipart/form-data; boundary=<calculated when request is sent>"
        super(JSONResponse,self).__init__(content, **kwargs)
csrf_exempt
def topping_list(request):
    if request.method == 'GET':
        toppings = Topping.objects.all()
        topping_serializer = ToppingSerializers(toppings, many = True)
        return JSONResponse(topping_serializer.data)
    
    elif request.method == 'POST':
        topping_data =  JSONParser().parse(request)
        topping_serializer = ToppingSerializers(data = topping_data)
        if topping_serializer.is_valid() :
            topping_serializer.save()
            return JSONResponse(topping_serializer.data,\
                status = status.HTTP_201_CREATED)
        return JSONResponse(topping_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
csrf_exempt
def topping_deltail(request, pk):
    try:
        topping = Topping.objects.get(pk = pk)
    except Topping.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        topping_serializer = ToppingSerializers(topping)
        return JSONResponse(topping_serializer.data)
    elif request.method == 'PUT':
        topping_data = JSONParser().parse(request)
        topping_serializer = ToppingSerializers(data = topping_data)
        if topping_serializer.is_valid:
            topping_serializer.save()
            return JSONResponse(topping_serializer.data)
        return JSONResponse(topping_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        topping.delete()
        return JSONResponse(status = status.HTTP_204_NO_CONTENT)
# def post(self, request):
#     mydata = ToppingSerializers(request.data)
#     name = mydata.data['name']
#     cost = mydata.data['cost']
#     countPizza = mydata.data['countPizza']
#     topping = Topping.objects.create(name=name, cost=cost, countPizza=countPizza)
#     return Response(data=topping.id,status=status.HTTP_200_OK)
csrf_exempt
def side_list(request):
    if request.method == 'GET':
        sides = SideDishes.objects.all()
        side_data = SideDishesSerializers(sides, many = True)
        return JSONResponse(side_data.data,)
    elif request.method == 'POST':
        side_data = JSONParser().parse(request)
        side_serializers = SideDishesSerializers(data = side_data)
        if side_serializers.is_valid():
            side_serializers.save()
            return JSONResponse(side_serializers.data, status = status.HTTP_201_CREATED)
        return JSONResponse(side_serializers.errors, status = status.HTTP_400_BAD_REQUEST)
csrf_exempt
def side_detail(request, pk):
    try:
        side = SideDishes.objects.get(pk=pk)
    except SideDishes.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        side_serializers = SideDishesSerializers(side)
        return JSONResponse(side_serializers.data)
    elif request.method == 'PUT':
        side_data = JSONParser().parse(request)
        side_serializers = SideDishesSerializers(data = side_data)
        if side_serializers.is_valid:
            side_serializers.save()
            return JSONResponse(side_serializers.data)
        return JSONResponse(side_serializers.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Topping.objects.delete(side)
        return JSONResponse(status = status.HTTP_204_NO_CONTENT)
csrf_exempt
def pizza_list(request):
    if request.method == 'GET':
        pizzas = Pizza.objects.all()
        pizza_data = PizzaSerializers(pizzas, many = True)
        return JSONResponse(pizza_data.data)
def pizza_detail(request,pk):
    try:
        pizza = Pizza.objects.get(pk = pk)
    except Pizza.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        pizza_serializers = PizzaSerializers(pizza)
        return JSONResponse(pizza_serializers.data)
csrf_exempt
def combo_list(request):
    if request.method == 'GET':
        combos = Combo.objects.all()
        combo_data = PizzaSerializers(combos, many = True)
        return JSONResponse(combo_data.data)
def combo_detail(request, pk):
    try:
        combo = Combo.objects.get(pk = pk)
    except Combo.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        combo_serializers = PizzaSerializers(combo)
        return JSONResponse(combo_serializers.data)

    
        




