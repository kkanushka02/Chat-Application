from django.contrib import admin
from django.urls import path
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('signup/', views.signup, name='signup'),  
    path('login/', views.login_view, name='login'),  
    path('chatroom/', views.chatroom, name='chatroom'),  
    path('logout/', views.logout_view, name='logout'), 
    path('messages/<int:user_id>/', views.messages_view, name='messages'),  
]
