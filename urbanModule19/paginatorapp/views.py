from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


# Create your views here.

def index(request):
    get_nums = SavedPostNums.objects.all()
    get_nums_list = []
    for i in get_nums:
        get_nums_list.append(i.number_of_posts)
    posts_on_page = request.POST.get('posts_on_page')
    posts = Post.objects.all().order_by('-created_at')
    # paginator = Paginator(posts, 4)
    if posts_on_page is not None:
        SavedPostNums.objects.all().delete()
        SavedPostNums.objects.create(number_of_posts=posts_on_page)
        paginator = Paginator(posts, posts_on_page)
    else:
        print(get_nums_list)
        paginator = Paginator(posts, get_nums_list[-1])
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})

# def index(request):
#     posts_on_page = request.POST.get('posts_on_page')
#     posts = Post.objects.all().order_by('-created_at')
#     # paginator = Paginator(posts, 4)
#     if posts_on_page is not None:
#         paginator = Paginator(posts, posts_on_page)
#     else:
#         paginator = Paginator(posts, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'index.html', {'page_obj': page_obj})
