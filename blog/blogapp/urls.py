from blogapp import views
from django.urls import path

urlpatterns = [
    path('',views.home_page),
    path('add',views.add_blog),
    path('edit',views.edit_blog),
    path('delete',views.delete_blog),
    path('user',views.user_info)
]