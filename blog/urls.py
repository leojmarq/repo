from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"), 
    path('', PostListView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail_view"),
    path("post/new",PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/delete", PostDetailView.as_view(), name="post_delete"),
]
