from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_created=True)
    update_at = models.DateField(auto_created=True)
   
    class Meta:
        abstract = True

class Product(BaseModel):
    product = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.IntegerField(default=0)

class ProductMetaInformation(BaseModel):
    product = models.OneToOneField(Product,on_delete=models.CASCADE, related_name="meta_info")
    product_measuring =models.CharField(max_length=100,null=True, blank=True,choices={("KG","KG"),("ML","ML"),("L","L")})
    product_quantity = models.CharField(max_length=100,null=True,blank=True)
    is_restrict = models.BooleanField(default=True)
    restrict_quantity = models.IntegerField()

class ProductImages(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    product_Image = models.ImageField(upload_to="Products")
     