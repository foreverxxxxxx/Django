from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import redirect,render
from django.urls import reverse
import datetime
data ={
   "telefon":["samsung s20","samsung s21"],
   "bilgisayar":["monster","casper"],
   "elektronik":[]
   
}
def index(request):
   # return HttpResponse("index") #We can connect to the database and return the product list
  # list_items =""
   categories=list(data.keys())
   """   
   for category in category_list:
       redirect_path= reverse("products_by_category",args=[category])
       list_items +=f"<li><a href=\"{redirect_path}\">{category}</a></li>"
   html=f"<ul>{list_items}</ul>"
   """
   return render(request,'index.html',{
      "categories":categories
   })
 #  return HttpResponse(html)
       


"""
def details(request):
    return HttpResponse("details")

def list (request):
    return HttpResponse("list")
"""
def getProductsByCategoryId(requst,category_id):
   # return  HttpResponse(category)
   category_list = list(data.keys())
   if category_id > len(category_list):
      return HttpResponseNotFound("yanlış kategori seçimi")
   category_name =category_list[category_id-1]
   redirect_path= reverse("products_by_category",args=[category_name])
   #return HttpResponseRedirect(redirect_path)
   return redirect(redirect_path)

def getProductsByCategory(request,category):
   try:
    products = data[category] #previous name category_text
    # return HttpResponse(category_text)
     #return HttpResponse(f"<h1>{category_text}</h1>")
     #We can define a dictionary data structure as the second parameter
    return render (request,'products.html',{ 
      "category" : category,
      "products": products,
      "now" : datetime.datetime.now()
     })
   except:
      return HttpResponseNotFound(f"<h1>yanlış kategori seçimi</h1>")



"""
    category_text=None
    if category == 'telefon':
        category_text="telefon kategorisindeki ürünler"
    elif category == 'bilgisayar':
        category_text="bilgisayar kategorisindeki ürünler"
    else :
        category_text = 'yanlış kategori seçimi'
    return HttpResponse(category_text)

def telefon (request):
    return HttpResponse("telefon kategorisindeki ürünler")

def bilgisayar (request):
    return HttpResponse("bilgisayar kategorisindeki ürünler")
"""