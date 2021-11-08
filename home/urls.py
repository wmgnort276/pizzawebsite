from django.urls import path
from . import views
app_name='home'
urlpatterns=[
    # path('', views.index,name='index'),
    path('', views.IndexView.as_view(), name='index1'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(),name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('', views.index1, name='index1'),
]