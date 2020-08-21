from django.shortcuts import render
from .models import Product,Category,Wishlist
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required



def home(request):
    if request.user.is_authenticated:
        return redirect('web:dashboard')
    category = Category.objects.all()
    product =Product.objects.all()
    return render(request,'home.html',{
        "category" : category,
        "product" : product,
    })

@login_required
def dashboard(request):
    product =Product.objects.all()
    return render(request,'web/dashboard.html',{
        "product" : product,
    })

def search(request):
    print('search eneterd')
    query = request.GET.get('query')
    print(query)
    if query is not None:
        result = Product.objects.filter(Q(title__icontains=query) | Q(price__icontains=query))
        print('if part',result)
    else:
        result = Product.objects.all()
        print('else part',result)
    return render(request,'home.html',{"product":result})

@login_required
def add_to_wishlist(request,pk):
    product = Product.objects.get(pk=pk)
    try:
        wishlist = Wishlist.objects.get(user=request.user)
        wishlist.products.add(product)
        wishlist.save()
    except:
        w = Wishlist.objects.create(user=request.user)
        w.products.add(product)
        w.save()
    return redirect('web:dashboard')

@login_required
def remove_from_wishlist(request,pk):
    product = Product.objects.get(pk=pk)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.products.remove(product)
    wishlist.save()

    return redirect("web:wishlist")

@login_required
def wishlist(request):
    w = Wishlist.objects.get(user=request.user)
    products = w.products.all()
    return render(request,'web/wishlist.html',{"products":products})

def product_detial(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request,'web/detail.html',{"product":product})
