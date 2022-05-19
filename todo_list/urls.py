from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.about, name = 'about'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegistrationView.as_view(), name='registration'),
    path('my_goals/', views.goal_list, name = 'goal_list'),
    path('goal/<int:pk>/', views.goal_detail, name='goal_detail'),
    path('goal/new/', views.goal_new, name='goal_new'),
    path('goal/<int:pk>/edit/', views.goal_edit, name='goal_edit'),
    path('goal/<int:pk>/delete/', views.goal_delete, name='goal_delete'),

]

