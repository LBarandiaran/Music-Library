from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.MusicList.as_view()),
    # path('int:pk>/', views.MusicDetail.as_view()),

]