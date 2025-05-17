from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64
from django.core.files.base import ContentFile
from .models import Lesson, UserRecording, LessonGroup

def lessons_list(request):
    """강의 그룹 목록 페이지"""
    lesson_groups = LessonGroup.objects.all()
    
    context = {
        'lesson_groups': lesson_groups
    }
    return render(request, 'lessons/list.html', context)

def group_detail(request, group_id):
    """강의 선택 페이지 (1강, 2강, 3강 등)"""
    group = get_object_or_404(LessonGroup, id=group_id)
    lessons = group.lessons.all().order_by('order')
    
    context = {
        'group': group,
        'lessons': lessons
    }
    return render(request, 'lessons/group_detail.html', context)

def lesson_detail(request, lesson_id):
    """강의 상세 페이지"""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    context = {
        'lesson': lesson
    }
    return render(request, 'lessons/lesson_detail.html', context)

def lesson_player(request, lesson_id):
    """강의 재생 페이지"""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    # 같은 그룹의 관련 강의 (최대 3개)
    if lesson.group:
        related_lessons = lesson.group.lessons.exclude(id=lesson_id).order_by('order')[:3]
    else:
        related_lessons = Lesson.objects.exclude(id=lesson_id).order_by('-created_at')[:3]
    
    context = {
        'lesson': lesson,
        'related_lessons': related_lessons,
    }
    return render(request, 'lessons/player.html', context)

@login_required
def recording(request, lesson_id):
    """녹음 페이지"""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    
    context = {
        'lesson': lesson,
    }
    return render(request, 'lessons/recording.html', context)

@login_required
def my_recordings(request):
    """내 녹음 목록 페이지"""
    recordings = UserRecording.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'recordings': recordings,
    }
    return render(request, 'lessons/my_recordings.html', context)

@csrf_exempt
@login_required
def save_recording(request):
    """녹음 저장 API"""
    if request.method == 'POST':
        try:
            lesson_id = request.POST.get('lesson_id')
            audio_file = request.FILES.get('audio_file')
            
            lesson = get_object_or_404(Lesson, id=lesson_id)
            
            # 파일 저장
            recording = UserRecording(
                user=request.user,
                lesson=lesson,
                recording_file=audio_file
            )
            recording.save()
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': '잘못된 요청입니다.'})
