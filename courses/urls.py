

from django.urls import path

from . import views

urlpatterns = [
	path('start', views.start, name='start'),
    path('index', views.index, name='index'),
    path('login', views.login_page, name='login_page'),
    path('create', views.create_page, name='create_page'),
    path('login_action', views.login_action, name='login_action'),
    path('login_api', views.login_api, name='login_api'),
    path('create_action', views.create_action, name='create_action'),
    path('<int:lesson_id>/view',views.display_lesson, name='display_lesson'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('<int:lesson_id>/display_quiz',views.display_quiz, name='display_quiz'),
    path('<int:lesson_id>/submit_quiz',views.submit_quiz, name='submit_quiz'),
]