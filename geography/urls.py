from django.urls import path
from . import views

app_name = 'geography'
urlpatterns = [
    path("", views.index, name="index"),
    path('<str:country>/<int:total>/<int:questions>/<path:continents>/answer/', views.answer, name='answer'),
    path('<str:country>/<path:continents>/reset/', views.reset, name='reset'),
    path('<int:total>/<int:questions>/filter/', views.filter, name='filter'),
]