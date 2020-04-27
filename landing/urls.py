from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.main_page, name='main_page'),
	path('project/page/<slug>/<pk>/', views.project_page, name='project_page'),
	path('about/', views.pages, {'template': 'landing/about_page.html'}, name='about_page'),
	path('page/', views.pages, {'template': 'landing/page.html'}, name='about_page'),
]