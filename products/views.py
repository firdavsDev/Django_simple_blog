from django.db.models import query
from django.shortcuts import render, get_object_or_404 #doentexcictlarni ushlash uchun 404

# Create your views here.


from django.http import Http404

from .models import Product

#form.py ichidan ProductForm
from .forms import ProductForm, RawProductForm


################################         1
def product_create_view(request):
    form=ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ProductForm()
    
    context = {
        'form':form
    }
    return render(request,"products/product_create.html",context)



###################################      2
# def product_create_view(request):
#     if request.method=='POST':
#         new_title=request.POST.get('title')
#         print(new_title)
#         #Product.objects.create(title=new_title)
#     context = {}
#     return render(request,"products/product_create.html",context)



#pretty form
# def product_create_view(request):
#     my_form=RawProductForm()
#     if request.method=='POST':
#         my_form=RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         'form':my_form
#     }
#     return render(request,"products/product_create.html",context)




def product_view(request):
    obj=Product.objects.all()
    
    context = {
        # 'title':obj.title,
        # 'description':obj.description
        'object':obj
    }
    # render ichida 1chi request sung html joyi sung
    return render(request,"products/product_detail.html",context)




def render_initial_data(request):
    initial_data={
        'title':'Bu mening ajoiyib title'
    }
    obj=Product.objects.get(id=20)
    form=Product(request.POST or None,instance=obj) #initial= bu orqali 
    if form.is_valid():
        form.save()
    context={
        'form':form
    }
    return render(request,"products/product_create.html",context)

# def dynamic_lookup_view(request,id):
#     #obj=Product.objects.get(id=id)
#     #obj=get_object_or_404(Product,id=id) #Xatolarni ushlab qolish uchun
#     try:
#         obj=Product.objects.get(id=id)
#         queryset=Product.objects.all() #List formatda productlarni
#         #obj.delete() uchirish uchun kerak buladi
#     except Product.DoesNotExist:
#         raise Http404 #agar usha fayl bulmasa ushlab qolish uchun kerak buladi
#     context={
#         "object":obj
#     }
#     return render(request,"products/product_create.html",context)


def dynamic_lookup_view(request,id):
    
    try:
        queryset=Product.objects.all() #List formatda productlarni
        #obj.delete() uchirish uchun kerak buladi
        obj=Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404 #agar usha fayl bulmasa ushlab qolish uchun kerak buladi
    context={
        "object_list":queryset,
        "object":obj
    }
    return render(request,"products/product_list.html",context)