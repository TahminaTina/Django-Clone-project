from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-new'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('drafts/', views.DraftListView.as_view(), name='post-draft-list'),
    path('post/<int:pk>/comment', views.add_comment, name='add-comment'),
    path('comment/<int:pk>/approve', views.comment_approve, name='comment-approve'),
    path('comment/<int:pk>/remove', views.comment_delete, name='comment-remove'),
    path('post/<int:pk>/publish', views.post_publish, name='post-publish'),

]