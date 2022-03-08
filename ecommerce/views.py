from django.shortcuts import render,redirect
from Product.models import BannerImages,Category,Product,Images,Variants,Size,Color
from ecommerce.models import Setting,ContactForm,ContactMessage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib import messages
from OrderApp.models import ShopCart
# Create your views here.
def home(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.price*p.quantity
    total_quan = 0
    for p in cart_product:
        total_quan += p.quantity
    slide_images=BannerImages.objects.all()
    setting=Setting.objects.get(id=1)
    men=Category.objects.filter(categorytype__contains='Men')
    kid=Category.objects.filter(categorytype__contains='Kid')
    new_product_men=Product.objects.filter(categorytype__contains='Men',status__contains='new')
    context={
            'slide_images':slide_images,
            'setting':setting,
            'men':men,
            'kid':kid,
            'new_product_men':new_product_men,
            'cart_product':cart_product,
            'total_amount':total_amount,
            'total_quan': total_quan}
    return render(request,'ecommerce/home.html',context)

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            data=ContactMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Profile details updated.')
            return redirect('contact')
    form=ContactForm
    context={
         'form':form
    }
    return render(request,'ecommerce/contact.html',context)

def product_detail(request,id):
    productb=Product.objects.all()
    setting=Setting.objects.all()
    images=Images.objects.filter(product_id=id)
    product=Product.objects.get(id=id)
    men=Category.objects.filter(categorytype__contains='Men')
    kid=Category.objects.filter(categorytype__contains='Kid')
    new_product_men=Product.objects.filter(categorytype__contains='Men',status__contains='new')
    context={
            'setting':setting,
            'product':product,
            'images':images,
            'productb':productb,
            'men':men,
            'kid':kid,
            'new_product_men':new_product_men}
    if product.variant!="None":
        if request.method=='POST':
            variant_id=request.POST.get('variantid')
            variant=Variants.objects.get(id=variant_id)
            colors=Variants.objects.filter(product_id=id,size_id=variant.size_id)
            sizes = Variants.objects.raw('SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id',[id])
            query += variant.title+' Size:' + str(variant.size) + ' Color:' + str(variant.color)
        else:
            variants = Variants.objects.filter(product_id=id)
            colors = Variants.objects.filter(product_id=id, size_id=variants[0].size_id)
            sizes = Variants.objects.raw('SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id', [id])
            variant = Variants.objects.get(id=variants[0].id)
        context.update({'sizes': sizes, 'colors': colors,
                        'variant': variant, 'query': query
                        })
    return render(request,'ecommerce/product_detail.html',context)

def ajaxcolor(request):
    data = {}
    if request.POST.get('action') == 'post':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        colors = Variants.objects.filter(product_id=productid, size_id=size_id)
        context = {
            'size_id': size_id,
            'productid': productid,
            'colors': colors,
        }
        data = {'rendered_table': render_to_string('ecommerce/color_list.html', context=context)}
        return JsonResponse(data)
    return JsonResponse(data)