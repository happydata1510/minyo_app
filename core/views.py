from django.shortcuts import render

# Create your views here.

def home(request):
    """홈페이지 뷰"""
    return render(request, 'core/home.html')

def about(request):
    """소개 페이지 뷰"""
    return render(request, 'core/about.html')
