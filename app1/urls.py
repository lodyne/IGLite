from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='app1-home'),
    # path('upload/',views.upload='app1-upload'),
    path('post/',views.post_list,name='app1-post-list'),
    path('post/upload/',views.upload_post,name='app1-upload-post'),
    path('search/',views.search,name='app1-search'),
    path('notification/',views.notification,name='app1-notification'),
    path('message/',views.message,name='app1-message'),
    path('profile/',views.profile,name='app1-profile')
]
