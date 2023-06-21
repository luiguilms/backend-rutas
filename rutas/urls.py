from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ruta', views.RutasView.as_view(), name='rutas'),
    path('ruta/<int:ruta_id>', views.RutaDetailView.as_view()),
    #path('movilidad/', views.MovilidadView.as_view(), name='movilidad-list'),
]