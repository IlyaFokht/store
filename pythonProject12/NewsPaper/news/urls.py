from django.urls import path, include
from .views import PostsList, PostsDetail,PostSearch,PostAdd,PostDelete,PostUpdate  # импортируем наше представление

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', PostsList.as_view()),
    path('<int:pk>/', PostsDetail.as_view(),name='post'),
    path('news/',PostsList.as_view()),
    path('news/search/', PostSearch.as_view(),name='search'),
    path('news/add/', PostAdd.as_view(),name='add'),
    path('delete/<int:pk>', PostDelete.as_view(), name='delete'),
    path('add/<int:pk>', PostUpdate.as_view(), name='add'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
]