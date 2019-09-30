from django.urls import path
from .views import (MovieList, MovieDetail, MovieCategory, MovieLanguage,
                    MovieSearch, MovieYear, MostWatched, RecentlyAdded,
                    TopRated)

app_name = 'movie'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('most_watched/', MostWatched.as_view(), name='most_watched'),
    path('recently_added/', RecentlyAdded.as_view(), name='recently_added'),
    path('top_rated/', TopRated.as_view(), name='top_rated'),
    path('<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    path('year/<int:year>', MovieYear.as_view(), name='movie_year'),
]
