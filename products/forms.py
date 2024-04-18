from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '너의 이름'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '설명'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '가격'})
        }
        


    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if commit:
            instance.save()
        return instance
        

