from django.urls import path
from . import views

urlpatterns = [
    path('api/directors/',views.DirectorList.as_view()),
    path('api/actors/',views.ActorList.as_view()),
    path('api/movies/',views.MovieList.as_view()),
    path('api/movies/<int:pk>',views.MovieDetail.as_view()),
]