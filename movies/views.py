from movies.models import Movie
from django.shortcuts import redirect, render

# Create your views here.

# 새로운 글 작성 페이지 반환
def new(request):
    return render(request, 'movies/new.html')

# 작성하면 models에 반영 => detail로 redirect
def create(request):
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')
    movie = Movie(title=title, overview=overview, poster_path=poster_path)
    movie.save()

    return redirect('movies:detail', movie.pk)

# 전체 영화 목록 페이지(HOME) 반환
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

# 세부 영화 페이지 반환
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

# 세부 영화 수정 페이지 반환
def edit(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/edit.html', context)

# 수정하면 models에 반영 => detail로 redirect
def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.title = request.POST.get('title')
    movie.overview = request.POST.get('overview')
    movie.poster_path = request.POST.get('poster_path')
    movie.save()

    return redirect('movies:detail', movie.pk)

# 삭제하면 models에 반영 => index로 redirect
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)

def search(request):
    query = request.GET.get('query')
    movies = Movie.objects.filter(title__icontains=query)
    print(movies)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context) 
