from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('leaderboard/', views.leaderboard,name='leaderboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login,name='login'),
    path('user_home/',views.user_home,name='user_home'),
    path('logout/', views.logout_view, name='logout'),
    path('play/',views.play,name='play'),
    path('submission-result/<int:attempted_question_pk>/', views.submission_result, name='submission_result' )

]
