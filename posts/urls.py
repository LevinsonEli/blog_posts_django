from django.urls import path
from . import views

urlpatterns = [
    path('editPost/<int:id>', views.editPost, name='editPost'),
    path('<int:id>', views.post, name='post'),
    path('', views.index, name='index'),
]