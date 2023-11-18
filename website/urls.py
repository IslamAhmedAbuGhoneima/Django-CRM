from django.urls import path
from . import views

# app_name used for solve problem of multipal apps 
# app_name = 'website'
# {% url 'website:home||logout' %}

urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_page,name='register'),
    path('record/<int:pk>/',views.record_page,name='record'),
    path('delete_record/<int:pk>/',views.delete_page,name='delete'),
    path('add_record/',views.record_form,name='add_record'),
    path('update/<int:pk>/',views.update_record,name='update'),
    ]