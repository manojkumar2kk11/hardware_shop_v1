from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    """
    Variant of a product (size, color, etc.). Useful when a product has multiple SKUs.
    """
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, blank=True)  # e.g. "Large / Blue"
    size = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  # override product price
    image = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} - {self.name or self.sku or 'default'}"


class Inventory(models.Model):
    """
    Track stock levels per product or variant and optional warehouse/location.
    """
    product = models.ForeignKey(Product, related_name='inventory', on_delete=models.CASCADE, null=True, blank=True)
    variant = models.ForeignKey(ProductVariant, related_name='inventory', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    low_stock_threshold = models.IntegerField(default=5)
    location = models.CharField(max_length=255, null=True, blank=True)  # e.g. 'Warehouse A'

    class Meta:
        verbose_name_plural = "Inventories"

    def __str__(self):
        target = self.variant or self.product
        return f"{target} — {self.quantity}"


class Review(models.Model):
    """
    Customer reviews for products.
    """
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255, null=True, blank=True)  # or link to AUTH_USER_MODEL
    rating = models.PositiveSmallIntegerField(default=5)  # 1-5
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} review by {self.user_name or 'anonymous'}"