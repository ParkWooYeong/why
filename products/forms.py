from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'content', 'price']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '너의 이름'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '설명'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '가격'})
        }
        


    def save(self, author):
        product_instance = super().save(commit=False)
        product_instance.author = author
        product_instance.save()
        return product_instance
        

