from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, reverse
from OrderApp.models import ShopCart,ShopingCartForm
from django.contrib import messages
from ecommerce.models import Setting

# Create your views here.
def Add_to_Shoping_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checking = ShopCart.objects.filter(
        product_id=id, user_id=current_user.id)
    if checking:
        control = 1
    else:
        control = 0

    if request.method == "POST":
        form = ShopingCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(
                    product_id=id, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, 'Your Product  has been added')
        return HttpResponseRedirect(url)
    else:
        if control == 1:
            data = ShopCart.objects.get(
                product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        messages.success(request, 'Your  product has been added')
        return HttpResponseRedirect(url)

def cart_details(request):
    current_user=request.user
    setting=Setting.objects.get(id=1)
    cart_product=ShopCart.objects.filter(user_id=current_user.id)
    total_item=cart_product.count()
    total_amount=0
    for p in cart_product:
        total_amount += p.product.price*p.quantity
    context = {
        'setting': setting,
        'cart_product': cart_product,
        'total_amount': total_amount,
        'total_item':total_item
    }
    return render(request,'ecommerce/cart_details.html',context)