from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'html1.htm')
def py(request):
    return render(request,'py.htm')
def java(request):
    return render(request,'java.htm')

