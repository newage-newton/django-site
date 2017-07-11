from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/', auth_views.LoginView.as_view(redirect_authenticated_user= True), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^user/', views.user, name='user'),
    url(r'^signup/', views.signup, name='signup'),
]