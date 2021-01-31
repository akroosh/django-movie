from django.urls import path
from .views import ListMovie, ListGenre, MovieDetail, CreateMovie, CreateGenre

urlpatterns = [
    path('', ListMovie.as_view()),
    path('genres/', ListGenre.as_view()),
    path('genres/create', CreateGenre.as_view()),
    path('<str:slug>', MovieDetail.as_view()),
    path('create/', CreateMovie.as_view())
]