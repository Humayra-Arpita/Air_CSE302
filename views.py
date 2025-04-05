from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,Templete_name='LavishBnB\home.html')

def home(request):
    return render(request,Templete_name='LavishBnB\products.html')

 def home(request):
    return render(request,Templete_name='LavishBnB\productsdetail.html')   