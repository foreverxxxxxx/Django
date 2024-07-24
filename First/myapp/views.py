
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect,render
from django.urls import reverse
# import datetime
from .models import Product
from.forms import ProductForm
# from django.db.models import Avg,Min,Max

# data ={
#    "telefon":["samsung s20","samsung s21"],
#    "bilgisayar":["monster","casper"],
#    "elektronik":[]
   
# }
def index(request):
    products = Product.objects.filter(isActive=True).order_by("-price")
    # product_count = Product.objects.filter(isActive=True).count()

    # price = Product.objects.filter(isActive=True).aggregate(
    #     avg_price=Avg("price"),
    #     min_price=Min("price"),
    #     max_price=Max("price")
    # )


    context ={ 
      "products":products
    #   "product_count":product_count,
    #   "price" : price
   }
   # return HttpResponse("index") #We can connect to the database and return the product list
  # list_items =""
  # categories=list(data.keys())
    """   
   for category in category_list:
       redirect_path= reverse("products_by_category",args=[category])
       list_items +=f"<li><a href=\"{redirect_path}\">{category}</a></li>"
   html=f"<ul>{list_items}</ul>"
   """
    return render(request,'index.html',context) 

def list(request):
    if 'q' in request.GET and request.GET.get('q'):
        q = request.GET['q']
        products = Product.objects.filter(name__contains=q).order_by("-price")
    else:
        products = Product.objects.all().order_by("-price")

    context = {
        "products": products,
    }

    return render(request, 'list.html', context)

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            # p = Product(name= form.cleaned_data["product_name"], 
            # description = form.cleaned_data["description"], 
            # price= form.cleaned_data["price"], 
            # imageUrl="1.jpg", 
            # slug=form.cleaned_data["slug"])
            # p.save()
            return redirect("product_list") 
        # product_name = request.POST['product_name']
        # price = request.POST['price']
        # description = request.POST['description']
        # slug = request.POST['slug']
        # error=False

        # if(product_name == "" or len(product_name)<=10 ):
        #    error=True
        
        # if(error):
        #     return render(request,"create.html",{
        #         "error":True
        #     })
        # else :
        # p = Product(name= product_name, description = description, price= price, imageUrl="1.jpg", slug=slug)
        # p.save()
        # return HttpResponseRedirect("list")
    else:
        form=ProductForm()
    
         
        
    return render(request, "create.html",{
        "form":form
    })


def edit(request,id):
    product=get_object_or_404(Product,pk=id)

    if request.method=="POST":
        form=ProductForm(request.POST,instance=product)

        if form.is_valid():
            form.save()
            return redirect("product_list")
        
    else:
        form=ProductForm(instance=product)

    return render(request,"edit.html",{
        "form":form
    })

def delete(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        product.delete()
        return redirect("product_list")

    return render(request, "delete-confirm.html", {
        "product": product
    })


def details(request,slug):
#    try:
#      product=Product.objects.get(pk=id)
#    except:
#       raise Http404

   product=get_object_or_404(Product,slug= slug) 
   context={
      "product":product
   }
   return render(request,"details.html",context)
   
 #  return HttpResponse(html)
       


"""
def details(request):
    return HttpResponse("details")

def list (request):
    return HttpResponse("list")
"""
# def getProductsByCategoryId(requst,category_id):
   # return  HttpResponse(category)
#    category_list = list(data.keys())
#    if category_id > len(category_list):
#       return HttpResponseNotFound("yanlış kategori seçimi")
#    category_name =category_list[category_id-1]
#    redirect_path= reverse("products_by_category",args=[category_name])
   #return HttpResponseRedirect(redirect_path)
#    return redirect(redirect_path)

# def getProductsByCategory(request,category):
#    try:
#     products = data[category] #previous name category_text
    # return HttpResponse(category_text)
     #return HttpResponse(f"<h1>{category_text}</h1>")
     #We can define a dictionary data structure as the second parameter
#     return render (request,'products.html',{ 
#       "category" : category,
#       "products": products,
#       "now" : datetime.datetime.now()
#      })
#    except:
#       return HttpResponseNotFound(f"<h1>yanlış kategori seçimi</h1>")



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