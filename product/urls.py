"""
Этот фрагмент кода представляет собой файл конфигурации URL для приложения product в Django. В этом файле определяются пути, по которым пользователи могут обращаться к различным страницам или функциональным возможностям приложения. Вот подробное описание его компонентов:

1. Импорт модулей
from django.urls import path: Импортирует функцию path из модуля django.urls, которая используется для определения маршрутов URL.
from product.views import *: Импортирует все представления из файла views.py приложения product, чтобы их можно было связать с соответствующими URL.
2. Пространство имен приложения
app_name = 'product': Устанавливает пространство имен для маршрутов этого приложения. Это полезно для избегания конфликтов имен маршрутов, когда в проекте используется несколько приложений с похожими именами маршрутов. При обращении к этим маршрутам в других частях проекта нужно будет использовать формат product:имя_маршрута.
3. Определение маршрутов URL
path('menu/', menu, name='menu'): Определяет маршрут по адресу /menu/ и связывает его с представлением menu. Этот маршрут может быть доступен под именем menu.
"""
from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
]
