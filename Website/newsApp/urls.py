from django.urls import path

from . import views

app_name = 'newsApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sources/', views.source, name='source'),
    path('category/', views.category, name='category'),
    path('topic/', views.topic, name='topic'),
]