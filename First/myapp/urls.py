from django.urls import path 
from.import views 

urlpatterns=[
    path('',views.index,name='index'),
    path('details',views.details,name='details'),
    path('list',views.list,name='list'),
    path('telefon',views.telefon,name='telefon'),
    path('bilgisayar',views.bilgisayar,name="bilgisayar"),
    path('<int:category>',views.getProductsByCategoryId),
     path('<str:category_id>',views.getProductsByCategory,name='products_by_category')

]
