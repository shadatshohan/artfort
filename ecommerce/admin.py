from django.contrib import admin
from ecommerce.models import Setting
from Product.models import BannerImages
# Register your models here.
admin.site.register(Setting)
admin.site.register(BannerImages)