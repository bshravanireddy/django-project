
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('multiple/', views.multiple, name='multiple'),
    path('forms/', views.forms, name='forms'),
    path('html/', views.html_view, name='html'),
    path('css/', views.css_view, name='css'),
    path('javascript/', views.javascript_view, name='javascript'),
    path('update/<int:abc>/', views.update, name='update'),
    path('delete/<int:abc>/', views.delete, name='delete'),
    path('html/update/<int:abc>/', views.update_html, name='update_html'),
    path('html/delete/<int:abc>/', views.delete_html, name='delete_html'),
    path('css/update/<int:abc>/', views.update_css, name='update_css'),
    path('css/delete/<int:abc>/', views.delete_css, name='delete_css'),
    path('javascript/update/<int:abc>/', views.update_javascript, name='update_javascript'),
    path('javascript/delete/<int:abc>/', views.delete_javascript, name='delete_javascript'),

]

