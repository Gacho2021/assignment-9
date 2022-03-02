from django.shortcuts import render, get_object_or_404
from .models import product, techType, Review 
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

def index(request):
 return render(request, 'club\index.html')

def products(request):
 product_list=product.objects.all()
 return render(request, 'club/product.html', {'product_list': product_list})
def productDetail(request, id):
  product=get_object_or_404(product, pk=id)
  return render(request, 'club/productdetail.html', {'product' : product})

@login_required
def newProduct(request):
 form=ProductForm

if request.method=='POST':
  Form=ProductForm(request.POST)

if form_is.valid():     
   post=form.save(commit=True)
   post.save()
   form=ProductForm()

else:
  form=ProductForm()
return(render(request, 'tech/newproduct.html', {': form'})

def loginmessage(request):
 return render(request, 'tech/loginmessage.html')


def logoutmessage(request):
 return render(request, 'tech/logoutmessage.html')
