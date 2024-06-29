from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect,render
from django.urls import reverse
data={
    "telefon kategorisindeki ürünler",
    "bilgisayar kategorisindeki ürünler",
    "elektronik kategorisindeki ürünler"
}

["telefon","bilgisayar","elektronik"]

def index(request):
    #return HttpResponse("How are you today ?")
    list_items =""
    category_list = list(data.keys())

    for category in  category_list: 
     redirect_path = reverse("products_by_category",args= [category])
     list_items += f"<li><a href=\"{redirect_path}\">{category}</a></li>"

    html= f"<ul>{list_items}</ul>"

    return HttpResponse(html)


def details (request):
    return HttpResponse("details")

def list(request):
    return HttpResponse("list")

def getProductsByCategoryId(request,category_id):
   # return HttpResponse(category)
   category_list=list(data.keys())
   if category_id > len(category_id):
      return HttpResponseNotFound("yanlış kategori seçimi")
   category_name = category_list[category_id-1]
   redirect_path = reverse("products_by_category",args= [category_name])
 #  return HttpResponseRedirect("/products/"+redirect_text)
   return HttpResponseRedirect(redirect_path )

def getProductsByCategory(request,category):
   # category_text=None
  #  if category == 'bilgisayar':
    #    category_text="bilgisayar kategorisindeki ürünler"
   # elif category == 'telefon':
      #  category_text="telefon kategorisindeki ürünler"
  #  else:
  #      category_text = 'yanlış kategori seçimi'
  try:
   category_text = data[category]
   return HttpResponse(category_text)
  except:
     return HttpResponseNotFound(<h1>(yanlış kategori seçimi)</h1>)
#def telefon (request):
 #   return HttpResponse("telefon kategorisindeki ürünler")

#def bilgisayar (request):
 #   return HttpResponse("bilgisayar kategorisindeki ürünler")