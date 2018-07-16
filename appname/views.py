from django.shortcuts import render
def appmain(request):
    return render(request, 'demo/randomart.html', {})
    #write your python code
# Create your views here.
