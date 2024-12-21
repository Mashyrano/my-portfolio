from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home),
    path('login', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]