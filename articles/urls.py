from django.urls import path    # path import
from . import views             # views import

urlpatterns = [
    path('', views.index),      # 연결시킬 view들
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
    path('<int:pk>/detail/', views.detail),
    path('<int:pk>/delete/', views.delete),
]
