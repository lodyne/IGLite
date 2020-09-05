from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='app1-home'),
    path('search/',views.search,name='app1-search'),
    path('notification/',views.notification,name='app1-notification'),
    path('message/',views.message,name='app1-message'),
    path('profile/',views.profile,name='app1-profile')
]
