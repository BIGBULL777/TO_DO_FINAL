from django.urls import path
from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.tasks ,name ='home') ,
    path('home',views.tasks,name ='home') ,
    path('new',views.newform),
    path('loggedout',views.logoutUser),
    path('login',views.loginUser,name = 'login'),
    path('signup',views.handleSignup, name = 'signup'),
    path('times/',views.times),
    # path('accounts', include('django.contrib.auth.urls')),
    path('social-auth', include('social_django.urls', namespace='social')),
    path('update_task/<int:pk>',views.Update_task,name = 'Update_task'),
    path('Delete_task/<int:pk>',views.Delete_task,name = 'Delete_task'),
    path('update_table/<int:pk>',views.Updatetable,name = 'Update_table')
]


