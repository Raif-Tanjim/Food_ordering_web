from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,blank=True,null=True)
    ordering = models.IntegerField(default=0)
   
    class Meta():
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)
    def __str__(self) -> str:
        return self.title
    def save(self, *args, **kwargs):
        # Generate a slug from the title when saving the object
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
    
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    class Meta:
        abstract = True

class Product(BaseModel):
    category = models.ForeignKey(Category, default= 'food', related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True,blank=True,null=True)
    product_description = models.TextField(blank=True, null=True)
    product_price = models.FloatField(default= None)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        # Generate a slug from the title when saving the object
        if not self.product_slug:
            self.product_slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
    
class ProductMetaInformation(BaseModel):
    title = models.OneToOneField(Product,on_delete=models.CASCADE, related_name="meta_info")
    MEASURING_CHOICES = (
    ('KG', 'Kilogram'),
    ('ML', 'Milliliter'),
    ('L', 'Liter'),
)

    product_measuring = models.CharField(max_length=100, null=True, blank=True, choices=MEASURING_CHOICES)
    product_quantity = models.CharField(max_length=100,null=True,blank=True)
    is_restrict = models.BooleanField(default=True)
    restrict_quantity = models.IntegerField()

class ProductImages(BaseModel):
    title = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    product_Image = models.ImageField(upload_to="Products")
     