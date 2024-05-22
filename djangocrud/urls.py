from django.urls import path
from tasks import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('guiones/', views.guiones, name='guiones'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('create_guion/', views.create_guion, name='create_guion'),
    path('guiones/<int:guion_id>/', views.guion_detail, name='guion_detail'),
    path('guiones/<int:guion_id>/completar/', views.complete_guion, name='complete_guion'),  # Asegúrate de tener esta línea
    path('guiones/<int:guion_id>/eliminar/', views.delete_guion, name='delete_guion'),
]
