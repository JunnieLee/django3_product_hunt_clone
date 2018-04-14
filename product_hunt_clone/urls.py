from django.contrib import admin
from django.urls import path, include #include쓸라면 이거 꼭 추가해줘야 함!
from products import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')), 
    path('products/', include('products.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 이미지 업로드 기능 쓰려면 이 코드 꼭 있어야 됨
    # 이 코드 추가하는거 말고도 settings 파일 들어가서 MEDIA_ROOT랑 MEDIA_URL 정해줘야 함! 
