from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.signup, name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('profile_update/', views.profile_update, name='change_profile'),
    path('new/image', views.new_post, name='newpost'),
    path('search/', views.search_profile, name='search'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)