from django.db import models

# Create your models here.
class Category(models.Model):
    status= (
        ('True','True'),
        ('False','False'))
    title=models.CharField(max_length=200)
    keywords=models.CharField(max_length=100)
    image=models.ImageField(blank=True,upload_to='category/')
    details=models.TextField()
    status=models.CharField(max_length=20,choices=status)
    slug=models.SlugField(null=True,unique=True)
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
        ('True', 'True'),
        ('False', 'False'),)
    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='product/')
    new_price = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=15)
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=3)
    variant = models.CharField(max_length=10, choices=VARIANTS, default='None')
    detail = models.TextField()
    status = models.CharField(max_length=20, choices=status)
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