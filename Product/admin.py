import admin_thumbnails
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from Product.models import Category,Product,Images,Color,Size,Variants
# Register your models here.
@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model=Images
    readonly_fields = ('id',)
    extra=1

class ProductVariantsInline(admin.TabularInline):
    model=Variants
    readonly_fields=('image_tag',)
    extra=1
    show_change_link=True

@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image','title','image_thumbnail']

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','category','status','image_tag']
    list_filter=['category']
    list_per_page=10
    search_fields=['title','new_price','detail']
    readonly_fields=('image_tag',)
    inlines=[ProductImageInline,ProductVariantsInline]
    prepopulated_fields={'slug':('title',)}

# color csv
class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name','code','color_tag']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Color.objects.update_or_create(
                    name = fields[0],
                    code = fields[-1],
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name','code']
class VariantsAdmin(admin.ModelAdmin):
    list_display = ['title','product','color','size','price','quantity','image_tag']

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Variants,VariantsAdmin)