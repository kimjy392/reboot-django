from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'jobs'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('result/', views.result, name='result'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)