from django.contrib import admin
from .models import BrandOffer,ProductOffer,CategoryOffer
# Register your models here.

admin.site.register(BrandOffer)
admin.site.register(CategoryOffer)
admin.site.register(ProductOffer)