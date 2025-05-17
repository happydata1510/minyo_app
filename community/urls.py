from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('<int:post_id>/', views.post_detail, name='detail'),
    path('create/', views.post_create, name='create'),
    path('<int:post_id>/edit/', views.post_edit, name='edit'),
    path('<int:post_id>/delete/', views.post_delete, name='delete'),
    path('<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
] 