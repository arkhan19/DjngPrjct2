from django.shortcuts import render,get_object_or_404
from . import templates
# Create your views here.

def main(request):
    return render(request, 'sitex/main.html' )