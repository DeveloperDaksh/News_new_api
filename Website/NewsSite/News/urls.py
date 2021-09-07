from django.urls import path
from . import views

app_name = 'News'
urlpatterns = [
    path('', views.index, name='index'),
    path('sources/', views.source, name='source'),
    path('category/', views.category, name='category'),
    path('general/', views.general, name='general'),
    path('source_news/', views.source_singlenews, name='source_news'),
    path('category_news/', views.category_singlenews, name='category_news'),
    path('news/', views.general_singlenews, name='news'),
    path('contact', views.contact, name='contact'),
]