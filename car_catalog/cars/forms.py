from django import forms
from .models import Car, CarPurchase

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'image', 'link']


# class CarPurchaseForm(forms.ModelForm):
#     class Meta:
#         model = CarPurchase
#         fields = ['car', 'accessories']


class CarPurchaseForm(forms.ModelForm):
    class Meta:
        model = CarPurchase
        fields = ['car', 'accessories']
        widgets = {'accessories': forms.CheckboxSelectMultiple}

    def clean_accessories(self):
        accessories = self.cleaned_data['accessories']
        if len(accessories) > 2:
            raise forms.ValidationError('You can select up to two accessories.')
        return accessories
