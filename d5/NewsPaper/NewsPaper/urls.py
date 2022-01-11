from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('news.urls')),
    path('sign/', include('sign.urls')),
    path('', include('protect.urls')),
    path('accounts/', include('allauth.urls')),

    # делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py) сами автоматически подключались когда мы их добавим.
]