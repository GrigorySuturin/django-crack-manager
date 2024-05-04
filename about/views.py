from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from .models import About, Category

menu = [
    {'title': 'Описание', 'url_name': 'about'},
    {'title': "Видео", 'url_name': 'videos'},
    {'title': "Приколы", 'url_name': 'all-jokes'},
    {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = About.objects.all()
    data = {
        'title': 'Crck3 lore',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'about/index.html', context=data)


def about(request):
    return render(request, 'about/about.html', {'title': 'О сайте', 'menu': menu})


def index2(request, c_id):
    if c_id == 4:
        raise Http404()
    if c_id > 4:
        return redirect('/')
    return HttpResponse(f'<h2>ГАЙД НА МИПО ДЛЯ НОВИЧКОВ</h2><p>id: {c_id}</p>')


def videos(request):
    return HttpResponse('<h1> Видео пока нет </h1>')


def prikoli(request, post_slug):
    post = get_object_or_404(About, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
    }
    return render(request, 'about/post.html', data)


def all_prikoli(request):
    return HttpResponse('<h1> No jokes </h1>')


def login(request):
    return HttpResponse('<h1> Авторизации пока нет </h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = About.objects.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'about/index.html', context=data)
