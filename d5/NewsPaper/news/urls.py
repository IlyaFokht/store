from django.urls import path, include
from .views import PostsList, PostsDetail,PostSearch,AddNews,DeleteNews,ChangeNews  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
#    path('', PostsList.as_view()),
    path('<int:pk>/', PostsDetail.as_view(),name='post'),
    path('news/',PostsList.as_view(),name='news'),
    path('news/search/', PostSearch.as_view(),name='search'),
    path('news/add/', AddNews.as_view(),name='add'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='delete'),
    path('add/<int:pk>', ChangeNews.as_view(), name='add'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
]