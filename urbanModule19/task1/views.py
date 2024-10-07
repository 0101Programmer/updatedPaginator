from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *


# Create your views here.

def main_page(request):
    main_title = 'videogames.net'
    main_header = 'Главная страница'
    main = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
        'main_title': main_title,
        'main_header': main_header,
        'main': main,
        'shop': shop,
        'cart': cart
    }
    return render(request, 'main_page.html', context)


def shop_page(request):
    shop_title = 'videogames.net'
    shop_header = 'Игры'
    main = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    get_games = Game.objects.all()
    current_games = []
    for i in get_games:
        current_games.append(f'{i.title} | {i.description}. Стоимость: {round((i.cost), 2)}')
    games_list = current_games
    buy = 'Купить!'
    back = 'Вернуться на главную'
    context = {
        'shop_title': shop_title,
        'shop_header': shop_header,
        'games_list': games_list,
        'buy': buy,
        'back': back,
        'main': main,
        'shop': shop,
        'cart': cart
    }
    return render(request, 'shop_page.html', context)


def cart_page(request):
    cart_title = 'videogames.net'
    cart_header = 'Товары в корзине'
    none = 'Извините, но ваша корзина пуста'
    back = 'Вернуться на главную'
    main = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
        'cart_title': cart_title,
        'cart_header': cart_header,
        'none': none,
        'back': back,
        'main': main,
        'shop': shop,
        'cart': cart
    }
    return render(request, 'cart_page.html', context)


def sign_up_by_html(request):
    get_users = Buyer.objects.all()
    users_name = []
    for i in get_users:
        users_name.append(i.name)
    users = users_name
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >= 18 and username not in users:
            info['form'] = [username, password, age]
            Buyer.objects.create(name=username, age=age, balance=int(age)*3)
            return HttpResponse(f'Привет, {username}')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            print(info['error'])
            return HttpResponse(f'Пароли не совпадают')
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            print(info['error'])
            return HttpResponse(f'Вы должны быть старше 18')
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            print(info['error'])
            return HttpResponse(f'Пользователь уже существует')
    return render(request, 'registration_page.html', context=info)


def sign_up_by_django(request):
    get_users = Buyer.objects.all()
    users_name = []
    for i in get_users:
        users_name.append(i.name)
    users = users_name
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                info['form'] = [username, password, age]
                Buyer.objects.create(name=username, age=age, balance=age*10)
                print(info['form'])
                return HttpResponse(f'Привет, {username}')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                print(info['error'])
                return HttpResponse(f'Пароли не совпадают')
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                print(info['error'])
                return HttpResponse(f'Вы должны быть старше 18')
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                print(info['error'])
                return HttpResponse(f'Пользователь уже существует')
    return render(request, 'registration_page.html', context=info)
