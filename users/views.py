"""
Этот фрагмент кода в файле views.py описывает две функции представления в Django, которые используются для обработки
 бронирования столиков в ресторане. Ниже приведено подробное описание каждой функции.

1. book_table
Функция book_table отвечает за обработку формы бронирования столика. Эта функция:

Метод запроса:

Если запрос является POST-запросом, значит, форма была отправлена пользователем. Форма передается в экземпляр BookingForm с данными request.POST.
Валидация формы:

form.is_valid(): Проверяет, прошла ли форма валидацию. Если форма валидна, данные сохраняются в базе данных с помощью метода form.save().
Перенаправление после успешного бронирования:

Если форма успешно сохранена, пользователь перенаправляется на страницу успеха бронирования с помощью redirect('users:sucses').
Отображение формы бронирования:

Если запрос является GET-запросом (пользователь только открыл страницу бронирования), функция инициализирует пустую форму BookingForm.
Форма отображается на странице users.html с помощью render(request, 'users.html', {'form': form}).
Пример сценария использования:

Пользователь заходит на страницу бронирования столика.
Видит форму, заполняет ее, и отправляет запрос.
Если форма заполнена корректно, данные сохраняются, и пользователь перенаправляется на страницу успеха.
"""
from django.shortcuts import render, redirect
from .form import BookingForm, ContactForm, LoginForm, CreationForm, ChangeFormUser, ChangePasswordForm
from django.contrib import auth



def book_table(request):
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:index')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:index')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('product:index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = CreationForm()
    return render(request, 'singup.html', {'form': form})


def profile(request):
    return render(request, 'profile.html', )


def personal_profile(request):
    return render(request, 'user_profile.html')


def user_change_profile(request):
    if request.method == 'POST':
        form = ChangeFormUser(instance=request.user,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ChangeFormUser()
    return render(request, 'user_chage_profile.html', {'form': form})

def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = ChangePasswordForm(user)
    return render(request, 'change_password.html', {'form': form})

