from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    """
    Represents a product category.
    """
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    ordering = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate a slug from the title when saving the object
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])

class BaseModel(models.Model):
    """
    Base model for common fields like created_at and updated_at.
    """
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(BaseModel):
    """
    Represents a product.
    """
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    product_price = models.FloatField(default=1)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Generate a slug from the title when saving the object
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

class ProductMetaInformation(BaseModel):
    """
    Represents additional information about a product.
    """
    title = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="meta_info")
    MEASURING_CHOICES = (
        ('KG', 'Kilogram'),
        ('ML', 'Milliliter'),
        ('L', 'Liter'),
    )

    product_measuring = models.CharField(max_length=100, null=True, blank=True, choices=MEASURING_CHOICES)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    is_restrict = models.BooleanField(default=True)
    restrict_quantity = models.IntegerField()

class ProductImages(BaseModel):
    """
    Represents images associated with a product.
    """
    title = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    product_image = models.ImageField(upload_to="Products")
