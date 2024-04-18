from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django_filters import rest_framework as filters

from .models import Movie
from permisson.CustomPermissions import CustomModelPermissions
from .permissions import IsOwnerOrReadOnly
from .serializers import MovieSerializer
from .pagination import CustomPagination
from .filters import MovieFilter


class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter

    def perform_create(self, serializer): #- overrides the CreateModelMixin's perform_create method
        # Assign the user who created the movie 
        
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Movie.objects.all()
        return Movie.objects.filter(creator=self.request.user)
        # OR we can use like this too... return Movie.objects.filter(creator__username=self.request.user.username)

class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, CustomModelPermissions]





