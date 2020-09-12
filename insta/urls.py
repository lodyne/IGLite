from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('',views.home,name='insta-home'),
    path('post/',views.post_list,name='insta-post_list'),
    path('post/upload/',views.upload_post,name='insta-upload_post'),
    path('search/',views.search,name='insta-search'),
    path('notification/',views.notification,name='insta-notification'),
    path('message/',views.message,name='insta-message'),
    path('profile/',views.profile,name='insta-profile')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)