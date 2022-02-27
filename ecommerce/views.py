from django.shortcuts import render
from Product.models import BannerImages
from ecommerce.models import Setting
# Create your views here.
def home(request):
	slide_images=BannerImages.objects.all()
	setting=Setting.objects.get(id=1)
	context={'slide_images':slide_images,'setting':setting}
	return render(request,'ecommerce/home.html',context)

def contact(request):
	pass