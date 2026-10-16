from django.shortcuts import render,redirect
from dashboard.models import*
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'home.html')

def products(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        description = request.POST.get('description')
        old_price = request.POST.get("old_price") or 0
        new_price = request.POST.get("new_price") or 0

        if old_price:
            old_price = float(old_price)
        else:
            old_price = 0

        if new_price:
            new_price = float(new_price)
        else:
            new_price = 0

        print("Image:", image)
        print("Name:", name)
        print("Description:", description)
        print("Old Price:", old_price)
        print("New Price:", new_price)


        Product.objects.create(
            image=image, 
            name=name, 
            description=description, 
            old_price=old_price,
            new_price=new_price)

    context = {
        'queryset': Product.objects.all()
    }
    return render(request, 'products.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        description = request.POST.get('description')
        old_price = request.POST.get("old_price") or 0
        new_price = request.POST.get("new_price") or 0

        if old_price:
            old_price = float(old_price)
        else:
            old_price = 0

        if new_price:
            new_price = float(new_price)
        else:
            new_price = 0

        print("Image:", image)
        print("Name:", name)
        print("Description:", description)
        print("Old Price:", old_price)
        print("New Price:", new_price)


        Product.objects.create(
            image=image, 
            name=name, 
            description=description, 
            old_price=old_price,
            new_price=new_price)

    context = {
        'queryset': Product.objects.all()
    }
    
    return render(request, 'dashboard.html', context)

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('dashboard')

def update_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        description = request.POST.get('description')
        old_price = request.POST.get("old_price") or 0
        new_price = request.POST.get("new_price") or 0

        if old_price:
            old_price = float(old_price)
        else:
            old_price = 0

        if new_price:
            new_price = float(new_price)
        else:
            new_price = 0

        product.image = image if image else product.image
        product.name = name
        product.description = description
        product.old_price = old_price
        product.new_price = new_price
        product.save()

        return redirect('dashboard')

    context = {
        'product': product
    }

    return render(request, 'update_product.html', context)




