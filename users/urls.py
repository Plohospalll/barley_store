"""
2. Пространство имен приложения
app_name = 'users': Устанавливает пространство имен для маршрутов этого приложения. Пространство имен помогает различать маршруты, если в проекте есть несколько приложений с одинаковыми именами маршрутов. Для ссылки на этот маршрут в шаблонах или других частях проекта нужно будет использовать формат users:имя_маршрута.
3. Определение маршрутов URL
path('users/', users, name='users'): Этот маршрут определяет, что при обращении пользователя по адресу /users/ будет вызвано представление users, которое должно быть определено в файле views.py приложения users.
URL-путь: 'users/' - это часть URL, которая следует за доменом сайта. Например, если ваш сайт расположен по адресу http://example.com, то этот маршрут будет доступен по адресу http://example.com/booking/.
Представление: users - функция или класс, определенные в views.py, которые обрабатывают запросы по этому URL.
Имя маршрута: name='users' - уникальное имя, присвоенное этому маршруту. Оно используется для создания ссылок на этот маршрут в шаблонах и других частях приложения.
4. Зачем это нужно?
Это конфигурация позволяет вашему приложению определять, какое представление следует использовать при посещении пользователем конкретного URL. В данном случае, при посещении URL /users/, будет вызвана функция users из файла views.py, которая может, например, отображать форму для резервирования стола или обрабатывать запрос на бронирование.
"""
import profile

from django.urls import path
from users.views import *
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('booking/', book_table, name='booking'),
    path('contact/',contact, name='contact'),
    path('login/', login, name='login'),
    path('register/',register, name='register'),
    path('profile/', profile, name='profile'),
    path('account/',personal_profile, name='account'),
    path('change/',user_change_profile, name='change'),
    path('password/', change_password, name='password'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]