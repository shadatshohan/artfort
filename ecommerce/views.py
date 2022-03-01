from django.shortcuts import render
from Product.models import BannerImages,Category,Product,Images
from ecommerce.models import Setting
# Create your views here.
def home(request):
	slide_images=BannerImages.objects.all()
	setting=Setting.objects.get(id=1)
	men=Category.objects.filter(categorytype__contains='Men')
	kid=Category.objects.filter(categorytype__contains='Kid')
	new_product_men=Product.objects.filter(categorytype__contains='Men',status__contains='new')
	context={'slide_images':slide_images,'setting':setting,'men':men,'kid':kid,'new_product_men':new_product_men}
	return render(request,'ecommerce/home.html',context)

def contact(request):
	return render(request,'ecommerce/contact.html')

def product_detail(request,id):
	product=Product.objects.all()
	setting=Setting.objects.all()
	images=Images.objects.filter(product_id=id)
	single_product=Product.objects.get(id=id)
	men=Category.objects.filter(categorytype__contains='Men')
	kid=Category.objects.filter(categorytype__contains='Kid')
	context={
            'setting':setting,
            'single_product':single_product,
            'images':images,
            'product':product,
            'men':men,
            'kid':kid}
	return render(request,'ecommerce/product_detail.html',context)