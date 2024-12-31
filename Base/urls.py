from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('', views.home),
    path('login', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('message', views.leave_message, name='message'),
    path('update_skill/<int:pk>', views.update_skill, name='update_skill'),
    path('delete_skill/<int:pk>', views.delete_skill, name='delete_skill'),
    path('create_skill', views.create_skill, name='create_skill'),
    path('update_project/<int:pk>', views.update_project, name='update_project'),
    path('delete_project/<int:pk>', views.delete_project, name='delete_project'),
    path('create_project', views.create_project, name='create_project'),
    path('edit_education/<int:pk>', views.edit_education, name='edit_education'),
    path('delete_education/<int:pk>', views.delete_education, name='delete_education'),
    path('create_education', views.create_education, name='create_education'),
    path('edit_me', views.edit_me, name='edit_me'),
    path('cv/<path:file_name>', views.serve_cv, name='serve_cv'),
]