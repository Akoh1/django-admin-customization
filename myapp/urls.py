from django.urls import path
from . import views
from . import custom

app_name = 'myapp'

# admin.site.login = custom.site.login

urlpatterns = [
    path('', views.admin_home, name='home'),
    path('new/user/', views.add_user, name='add-user'),
    path('send-emails/', views.send_email, name='send-emails'),
    path('change-status/<int:id>/', views.change_status, name='change-status'),
]