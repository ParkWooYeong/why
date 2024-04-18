from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from products.forms import ProductForm
from products.models import Product
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def list_view(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})

@login_required
def create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user  
            product.save()
            return redirect("products:list")
    else:
        form = ProductForm()
    return render(request, "products/create.html", {'form': form})

def detail_view(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/detail.html", {"product": product})

@login_required
def update_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    
    if product.author != request.user:
        return redirect("products:detail", product_id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            updated_product = form.save(commit=False)  
            updated_product.author = request.user      
            updated_product.save()               
            return redirect("products:list")
    else:
        form = ProductForm(instance=product)

    return render(request, "products/create.html", {"form": form})


@login_required
@require_POST
def delete_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.author != request.user:
        messages.warning(request,"작성자 본인만 수정")
        return redirect("products:detail", product_id=product_id)
    product.delete()
    return redirect("products:list")


@login_required
@require_POST
def choose_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user: User = request.user
    if user.choose_products.filter(id=product_id).exists():
        user.choose_products.remove(product)
    else:
        user.choose_products.add(product)
    return redirect('products:list')

def upload_image(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('some_view')
    else:
        form = ProductForm()
    return render(request, 'upload_image.html', {'form': form})
