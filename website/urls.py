
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('update-delete/<int:pk>/', views.update_delete_record, name='update_delete'),
    path('update/<int:pk>/', views.update_user_record, name='update'),
    path('delete/<int:pk>/', views.delete_user_record, name='delete'),
    path('record/', views.add_user_record, name='record'),
]
