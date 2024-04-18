from django.urls import path
from . import views

# http://localhost:8000/api/v1/movies/?ordering=id&page=1&page_size=10
urlpatterns = [
    path('/', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('/<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
]