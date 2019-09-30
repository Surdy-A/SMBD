from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie, MovieLinks


class HomeView(ListView):
    model = Movie
    template_name = "movie/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status='MW')
        context['recently_added'] = Movie.objects.filter(status='RA')
        return context


class MostWatched(ListView):
    model = Movie
    template_name = "movie/most_watched.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(MostWatched, self).get_context_data(**kwargs)
        context['most_watched'] = Movie.objects.filter(status='MW')
        return context


class RecentlyAdded(ListView):
    model = Movie
    template_name = "movie/recently_added.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(RecentlyAdded, self).get_context_data(**kwargs)
        context['recently_added'] = Movie.objects.filter(status='RA')
        return context


class TopRated(ListView):
    model = Movie
    template_name = "movie/top_rated.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TopRated, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        return context


class MovieList(ListView):
    model = Movie
    paginate_by = 3


class MovieDetail(DetailView):
    model = Movie

    def get_Object(self):
        object = super(MovieDetail, self).get_object()
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        context['related_movies'] = Movie.objects.filter(
            category=self.get_object().category)
        return context


class MovieCategory(ListView):
    model = Movie
    paginate_by = 3

    def get_queryset(self):
        self.category = self.kwargs['category']
        movies = Movie.objects.filter(category=self.category)
        return movies

    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context


class MovieLanguage(ListView):
    model = Movie
    paginate_by = 1

    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context


class MovieSearch(ListView):
    model = Movie
    paginate_by = 1

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = Movie.object.filter(title_icontains=query)

        else:
            object_list = self.model.objects.none()

        return object_list


class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True