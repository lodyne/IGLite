from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views


urlpatterns = [
    # path('', views.home, name='insta-home'),
    # path('post/', views.post_list, name='insta-post_list')

    # * urls for class-based view

    path('', PostListView.as_view(), name='insta-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    #####################################

    path('post/upload/', views.upload_post, name='insta-upload_post'),
    path('search/', views.search, name='insta-search'),
    path('notification/', views.notification, name='insta-notification'),
    path('message/', views.message, name='insta-message'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
