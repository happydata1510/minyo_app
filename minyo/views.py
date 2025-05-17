from django.shortcuts import render, get_object_or_404
from .models import Minyo, Category

def minyo_list(request):
    """민요 목록 페이지"""
    categories = Category.objects.all()
    minyos = Minyo.objects.all().order_by('-created_at')
    
    context = {
        'categories': categories,
        'minyos': minyos,
    }
    return render(request, 'minyo/list.html', context)

def minyo_player(request, minyo_id):
    """민요 재생 페이지"""
    minyo = get_object_or_404(Minyo, id=minyo_id)
    related_minyos = Minyo.objects.filter(category=minyo.category).exclude(id=minyo_id)[:3]
    
    context = {
        'minyo': minyo,
        'related_minyos': related_minyos,
    }
    return render(request, 'minyo/player.html', context)

def category_view(request, category_id):
    """카테고리별 민요 목록"""
    category = get_object_or_404(Category, id=category_id)
    minyos = Minyo.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.all()
    
    context = {
        'category': category,
        'categories': categories,
        'minyos': minyos,
    }
    return render(request, 'minyo/list.html', context)
