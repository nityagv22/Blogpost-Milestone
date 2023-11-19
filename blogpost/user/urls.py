from . import views
from django.urls import path
app_name= 'user'
urlpatterns = [
    path('',views.userlist,name='user list'),
    path('<int:user_id>/',views.userdetails,name='details')
 

]