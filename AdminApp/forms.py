
from django import forms
from django.db import models
from django.db.models import fields
from django.forms.fields import FileField
from django.forms.widgets import CheckboxInput, FileInput, TextInput
from coupon.models import Coupon
from offer.models import BrandOffer, CategoryOffer, ProductOffer
from category.models import category

from store.models import Banners, Product, Variation
from brands.models import Brand

class EditProduct(forms.ModelForm):
    product_name = forms.CharField(required=True,max_length=200,widget=forms.TextInput(attrs={'placeholder':'product_name'}))
    description = forms.CharField(required=True,max_length=500,widget=forms.Textarea(attrs={'placeholder':'description'}))
    price = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'placeholder':'price'}))
    # images = forms.ImageField(required=True,widget=FileInput)
    stock = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'placeholder':'stock'}))
    is_available = forms.BooleanField(required = True,widget=CheckboxInput(attrs={'placeholder':'Status'}))
    

    class Meta: 
        model = Product
        fields = ['product_name','description','price','images','images1','images2','images3','stock','is_available','category']   

    def _init_(self, *args, **kwargs):
        super(EditProduct, self)._init_(*args, **kwargs) # images = forms.ImageField(required=True,widget=FileInput)



class EditBrand(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name','slug','logo','description']


class EditCategory(forms.ModelForm):
    class Meta:
        model = category
        fields = ['category_name','slug','cat_image']


class EditVarient(forms.ModelForm):
    class Meta:
        model = Variation
        fields =['product','variation_category','variation_value','color_name','is_active']
        widgets = {
   'variation_value': TextInput(attrs = {
      'type': 'color'
   }),
}

class EditBrandOffer(forms.ModelForm):
    class Meta:
        model = BrandOffer
        fields = ['brand_name', 'discount']


class EditCategoryOffer(forms.ModelForm):
    class Meta:
        model = CategoryOffer
        fields = ['category_name', 'discount']


class EditProductOffer(forms.ModelForm):
    class Meta:
        model = ProductOffer
        fields = ['product_name', 'discount']


class EditBanner(forms.ModelForm):
    class Meta:
        model = Banners
        fields = ['image', 'product','alt_text']


class EditCoupon(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['coupon_name', 'code','coupon_limit','valid_from','valid_to','discount']