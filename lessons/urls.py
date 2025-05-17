from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('', views.lessons_list, name='list'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
    path('<int:lesson_id>/', views.lesson_detail, name='detail'),
    path('<int:lesson_id>/recording/', views.recording, name='recording'),
    path('my-recordings/', views.my_recordings, name='my_recordings'),
    path('save-recording/', views.save_recording, name='save_recording'),
] 