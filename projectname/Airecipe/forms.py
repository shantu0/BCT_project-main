from django import forms
from .models import WishlistItem

class WishlistItemForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = ['item_name', 'description']
