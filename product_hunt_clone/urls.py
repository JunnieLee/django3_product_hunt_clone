from django.contrib import admin
from django.urls import path, include #include쓸라면 이거 꼭 추가해줘야 함!
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')), 
]

