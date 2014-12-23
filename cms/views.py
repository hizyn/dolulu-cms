from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, Post

import random

def category(request, pk):
    dreams = Post.objects.filter(category=pk, status=0)
    cates = Category.objects.filter(is_nav=True)
    category = get_object_or_404(Category, id=pk)
    hot_posts = Post.objects.order_by('-click')[:8]
    random_posts = random.sample(Post.objects.all(), 8)
    context = {
        'dreams': dreams, 
        'category': category, 
        'cates': cates,
        'hot_posts': hot_posts,
        'random_posts': random_posts,
    }

    return render(request, 'cms/category.html', context)


def index(request):
    cates = Category.objects.filter(is_nav=True)
    people_dreams = Post.objects.filter(category=1, status=0).order_by('-id')
    animal_dreams = Post.objects.filter(category=2, status=0).order_by('-id')
    plant_dreams = Post.objects.filter(category=3, status=0).order_by('-id')
    good_dreams = Post.objects.filter(category=4, status=0).order_by('-id')
    activity_dreams = Post.objects.filter(category=5, status=0).order_by('-id')
    life_dreams = Post.objects.filter(category=6, status=0).order_by('-id')
    nature_dreams = Post.objects.filter(category=7, status=0).order_by('-id')
    ghost_dreams = Post.objects.filter(category=8, status=0).order_by('-id')
    build_dreams = Post.objects.filter(category=9, status=0).order_by('-id')
    pregnant_dreams = Post.objects.filter(category=10, status=0).order_by('-id')
    other_dreams = Post.objects.filter(category=11, status=0).order_by('-id')
    hot_posts = Post.objects.order_by('-click')[:8]
    random_posts = random.sample(Post.objects.all(), 8)
    context = {
        'cates': cates, 
        'animal_dreams': animal_dreams,
        'people_dreams': people_dreams,
        'plant_dreams': plant_dreams,
        'good_dreams': good_dreams,
        'activity_dreams': activity_dreams,
        'life_dreams': life_dreams,
        'nature_dreams': nature_dreams,
        'ghost_dreams': ghost_dreams,
        'build_dreams': build_dreams,
        'pregnant_dreams': pregnant_dreams,
        'other_dreams': other_dreams,
        'hot_posts': hot_posts,
        'random_posts': random_posts,
    }
    return render(request, 'cms/index.html', context)


def post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.click += 1
    post.save()
    cates = Category.objects.filter(is_nav=True)
    hot_posts = Post.objects.order_by('-click')[:8]
    random_posts = random.sample(Post.objects.all(), 8)
    relate_dreams = Post.objects.filter(category=post.category)

    context = {
        'post': post, 
        'cates': cates, 
        'hot_posts': hot_posts,
        'random_posts': random_posts,
        'relate_dreams': relate_dreams,
        }
    if post.category.id == 10:
        return render(request, 'cms/pregnant_post.html', context)
    else:
        return render(request, 'cms/post.html', context)


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        dreams = Post.objects.filter(title__icontains=q, status=0)
        hot_posts = Post.objects.order_by('-click')[:8]
        random_posts = random.sample(Post.objects.all(), 8)
        cates = Category.objects.filter(is_nav=True)
        context = {
            'dreams': dreams,
            'q': q,    
            'hot_posts': hot_posts,
            'random_posts': random_posts,
            'cates': cates, 
        }
        return render(request, 'cms/search.html', context)
    else:
        hot_posts = Post.objects.order_by('-click')[:8]
        cates = Category.objects.filter(is_nav=True)
        random_posts = random.sample(Post.objects.all(), 8)
        context = {
            'error': True,    
            'cates': cates, 
            'hot_posts': hot_posts,
            'random_posts': random_posts,
        }
        return render(request, 'cms/search.html', context)

