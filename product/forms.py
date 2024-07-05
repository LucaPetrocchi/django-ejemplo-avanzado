from django import forms

from product.models import(
    Product,
    Category,
    Supplier,
    ProductReview,
    PriceHistory,
    ProductImage,
)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'category',
            'stock',
        ]
        
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                    'style': 'color: red',
                    }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    }
            ),
        }

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = [
            'author',
            'text',
            'rating',
            'product',
        ]
        
        widgets = {
            'product': forms.Select(
                attrs={
                    'class': 'form-control',
                    'readonly': 'readonly',
                }
            )
        }
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     self.fields['product'].initial = self.instance.product.id
    #     self.fields['author'].initial =  self.instance.author.id
    
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = [
            'product',
            'image',
            'description',
        ]