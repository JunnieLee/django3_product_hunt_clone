from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('detail/<int:product_id>/', views.detail, name='detail'),
    path('upvote/<int:product_id>', views.upvote, name='upvote'),
    path('upvote_at_home/<int:product_id>', views.upvote_at_home, name='upvote_at_home'),
] 
