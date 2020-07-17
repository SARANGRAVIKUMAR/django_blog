from django.urls import path

from . import views

urlpatterns = [
    # path('',views.home,name="blog-home"),
    path('', views.PostListView.as_view(template_name='home.html'), name="blog-home"),
    path('user/<str:username>', views.UserPostListView.as_view(template_name='user_post.html'), name="user-posts"),
    path('about/', views.about, name="blog-about"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(template_name='post_forms.html'), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(template_name='post_forms.html'), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(template_name="post_confirm_delete.html"),
         name='post-delete'),
]
