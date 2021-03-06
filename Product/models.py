from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
class Category(models.Model):
    categorytype= (
        ('Men','Men'),
        ('Kid','Kid'))
    categorytype=models.CharField(max_length=20,choices=categorytype,default="Fun")
    title=models.CharField(max_length=200)
    keywords=models.CharField(blank=True,max_length=100)
    image=models.ImageField(blank=True,upload_to='category/')
    details=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
        else:
            return ""
    image_tag.short_description = 'Image'

class Product(models.Model):
    status = (
        ('new', 'new'),
        ('best', 'best'),
        ('special','special'),)
    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )
    categorytype= (
        ('Men','Men'),
        ('Kid','Kid'))
    categorytype=models.CharField(max_length=20,choices=categorytype,default="Fun")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(blank=True,max_length=100)
    image = models.ImageField(blank=True, upload_to='product2/')
    image2=models.ImageField(blank=True, upload_to='product2/',default='product2/11.jpg')
    old_price = models.DecimalField(null=True,blank=True,decimal_places=2, max_digits=15)
    price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    discount=models.IntegerField(null=True,blank=True,default=0)
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=1)
    variant = models.CharField(max_length=10, choices=VARIANTS, default='None')
    detail = models.TextField()
    status = models.CharField(blank=True,max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'Image'

class BannerImages(models.Model):
    title = models.CharField(max_length=200,default="THE BIGGEST")
    desc=models.TextField(default="Special For Today",blank="True")
    image = models.ImageField()

    def __str__(self):
        return self.title

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='product2/')

    def __str(self):
        return self.title

class Color(models.Model):
    name=models.CharField(max_length=20)
    code=models.CharField(max_length=10,blank=True,null=True)
    def __str__(self):
        return self.name
    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""

class Size(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True,null=True)
    def __str__(self):
        return self.name

class Variants(models.Model):
    title=models.CharField(max_length=100,blank=True,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE,blank=True,null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,blank=True,null=True)
    image_id = models.IntegerField(blank=True,null=True,default=0)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)

    def __str__(self):
        return self.title

    def image(self):
        img=Images.objects.get(id=self.image_id)
        if img.id is not None:
            varimage=img.image.url
        else:
            varimage=""
        return varimage

    def image_tag(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
             return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
        else:
            return ""
