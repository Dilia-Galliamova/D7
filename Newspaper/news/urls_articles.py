from django.urls import path
from .views import PostsList, ArticleCreate, ArticleUpdate, ArticleDelete

urlpatterns = [
   path('', PostsList.as_view(), name='posts'),
   path('create/', ArticleCreate.as_view(), name='article_create'),
   path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
   path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]