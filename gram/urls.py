from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns=[
    re_path(r'^$',views.home,name='home'),
    path('register/',views.signup, name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('profile_update/', views.profile_update, name='change_profile'),
    re_path(r'^new/image$', views.post, name='post'),
    path('search/', views.search_profile, name='search'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)