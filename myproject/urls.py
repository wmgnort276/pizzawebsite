"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from myproject.profiles import views
# from myproject.project.views import ComboList
from profiles import views as profiles_view
from django.contrib.auth import views as auth_views
from project import views as project_view
from home import views as home_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('register/',profiles_view.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="profiles/login.html"),
    name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="profiles/logout.html"),
    name="logout"),
    path('forgotpassword/',auth_views.PasswordResetView.as_view(template_name="profiles/forgot.html"),name="forgot"),
    path('forgot/done/',auth_views.PasswordResetDoneView.as_view(template_name="profiles/forgot_done.html"),name="forgot-done"),
    path('forgot/confirm/',auth_views.PasswordResetConfirmView.as_view(template_name="profiles/forgot_confirm.html"),
    name="forgot-confirm"),
    path('forgot/complete/',auth_views.PasswordResetCompleteView.as_view(template_name="profiles/forgot_complete.html"),
    name="forgot-complete"),
    #API cũ
    path('topping/',project_view.topping_list),
    path('topping/<int:pk>/',project_view.topping_deltail),
    path('sidedishes/', project_view.side_list),
    path('sidedishes/<int:pk>/',project_view.side_detail),
    path('pizza/',project_view.pizza_list),
    path('pizza/<int:pk>/',project_view.pizza_detail),
    # path('toppings/',project_view.ToppingList.as_view(), name = project_view.ToppingList.name),
    # path('toppings/<int:Pk>',project_view.ToppingDetail.as_view(), name = project_view.ToppingDetail.name),
    # path('toppingamount/',project_view.ToppingAmountList.as_view()),
    # path('toppingamount/<int:pk>/',project_view.ToppingAmountDetail.as_view()),
    ## path('combo/',project_view.combo_list),
    ## path('combo/<int:pk>/', project_view.combo_detail),
    #Code API mới

    path('combo/',project_view.ComboList.as_view(), name = project_view.ComboList.name),
    path('combo/<int:pk>/', project_view.ComboDetail.as_view(), name = project_view.ComboDetail.name),
    path('amount/',project_view.ComboAmountList.as_view(), name = project_view.ComboAmountList.name),
    path('side/',project_view.SideDishesList.as_view(), name = project_view.SideDishesList.name),
    path('side/<int:pk>/', project_view.SideDishesDetail.as_view(), name = project_view.SideDishesDetail.name),
    path('amount/<int:pk>/', project_view.ComboAmountDetail.as_view(), name = project_view.ComboAmountDetail.name),
    path('toppings/',project_view.ToppingList.as_view(), name = project_view.ToppingList.name),
    path('toppings/<int:pk>/',project_view.ToppingDetail.as_view(), name = project_view.ToppingDetail.name),
    path('toppingamount/',project_view.ToppingAmountList.as_view(), name=project_view.ToppingAmountList.name),
    path('toppingamount/<int:pk>/',project_view.ToppingAmountDetail.as_view(), name = project_view.ToppingAmountDetail.name),
    path('piza/',project_view.PizzaList.as_view(), name=project_view.PizzaList.name),
    path('piza/<int:pk>/',project_view.PizzaDetail.as_view(), name=project_view.PizzaDetail.name),
    # path('side/<str:type>/',project_view.SideDishesDetail.as_view(), name=project_view.SideDishesDetail.name)
    # path('',project_view.APIRoot.as_view(), name = project_view.APIRoot.name)
    
    #API Profile
    path('profile/<int:pk>/',profiles_view.ProfileDeltail.as_view(), name=profiles_view.ProfileDeltail.name),
    path('choice/<int:pk>/',home_view.ChoiceDetails.as_view(), name = home_view.ChoiceDetails.name ),
    # path('question/<int:pk>/',home_view.QuestionDetail.as_view(),name=home_view.QuestionDetail.name),
    path('test/<int:pk>/',home_view.TestDetail.as_view(), name = home_view.TestDetail.name),
    path('combocategory/',project_view.ComboCategoryList.as_view(), name = project_view.ComboCategoryList.name),
    path('combocategory/<int:pk>/',project_view.ComboCategoryDetail.as_view(), name = project_view.ComboCategoryDetail.name)
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
