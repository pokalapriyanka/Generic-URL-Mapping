from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return render(request,'msd.html')
def rutu(request):
    return HttpResponse('He is the caption of CSK')