from django.contrib import admin
from Product.models import Category,Product,Images
# Register your models here.
class ProductImageInline(admin.TabularInline):
	model=Images
	extra=5

class ProductAdmin(admin.ModelAdmin):
	list_display=['title','status','created_at','updated_at','image_tag']
	list_filter=['title','created_at']
	list_per_page=10
	search_fields=['title','new_price','detail']
	inlines=[ProductImageInline]
	prepopulated_fields={'slug':('title',)}
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)