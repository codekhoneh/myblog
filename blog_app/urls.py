from django.urls import path
from .import views

app_name = 'blog'
urlpatterns = [path('detail/<slug:slug>',views.post_detail,name='article_detail'),
               path('all artikle',views.allarticle_list,name='articles_list'),
               path('categori/<int:pk>',views.category_detail,name='categor_detail'),
               path('search/',views.search,name='search_articles'),
               
               ]