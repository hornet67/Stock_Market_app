from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Stockdata
from .forms import StockdataForms

# Create your views here.
def home(request):
    data = Stockdata.objects.all()
    return render(request,'Home.html', {'data': data})



def update(request, id):
    stockdata = Stockdata.objects.get(id=id)

    formdata = StockdataForms(request.POST or None, instance=stockdata)
    if formdata.is_valid():
        formdata.save()
        messages.success(request, 'Data is updated succesfully.')
        return redirect('home')

    return render(request, 'update.html', {'form': formdata})

def deleted(request,id):
    record =  Stockdata.objects.get(pk=id)
    record.delete()
    return redirect('home')  
            
            
        
    

    
