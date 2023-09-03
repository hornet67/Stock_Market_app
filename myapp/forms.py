from django import  forms
from .models import Stockdata

class StockdataForms(forms.ModelForm):
    class  Meta:
        model = Stockdata
        fields = '__all__'
        wigets = {
            'date': forms.TextInput(attrs={'class':'form-control'}),
            'trade_code': forms.TextInput(attrs={'class':'form-control'}),
            'high': forms.TextInput(attrs={'class':'form-control'}),
            'low': forms.TextInput(attrs={'class':'form-control'}),
            'open': forms.TextInput(attrs={'class':'form-control'}),
            'close': forms.TextInput(attrs={'class':'form-control'}),
            'volume': forms.TextInput(attrs={'class':'form-control'})
             
        }