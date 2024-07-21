from django.urls import path 
from. import views

# http://127.0.0.1:8000/         => index
# http://127.0.0.1:8000/details  => details
# http://127.0.0.1:8000/list     => list

urlpatterns=[
    path('',views.index),
    path('index',views.index),
   # path('details',views.details,name='details'),
   # path('list',views.list,name='list'),
   # path('telefon',views.telefon),
   # path('bilgisayar',views.bilgisayar),
    path('<slug:slug>',views.details,name="product_details"),
    path('<int:category_id>',views.getProductsByCategoryId),
    path('<str:category>',views.getProductsByCategory,name='products_by_category') #The order of the url patterns is also important.
  
]