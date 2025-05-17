from django.urls import path
from . import views

app_name = 'minyo'

urlpatterns = [
    path('', views.minyo_list, name='list'),
    path('<int:minyo_id>/', views.minyo_player, name='player'),
    path('category/<int:category_id>/', views.category_view, name='category'),
] 