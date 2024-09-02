"""
Этот фрагмент кода представляет собой файл конфигурации URL для проекта на Django. В нем определяются правила маршрутизации URL, которые направляют запросы к соответствующим представлениям или приложениям внутри проекта. Вот подробное описание его компонентов:

1. Импорт модулей
from django.contrib import admin: Импортирует административную панель Django, позволяющую управлять моделями через веб-интерфейс.
from django.conf.urls.static import static: Импортирует функцию static, которая используется для обслуживания медиафайлов во время разработки.
from django.urls import path, include: Импортирует функцию path для определения маршрутов и функцию include для подключения конфигураций других приложений.
from product.views import *: Импортирует все представления из приложения product, чтобы маршрутизировать запросы на эти представления.
2. Определение маршрутов URL
path('admin/', admin.site.urls): Определяет маршрут для административной панели Django по адресу /admin/.
path('', index, name='index'): Определяет корневой маршрут (/) и привязывает его к представлению index. Этот маршрут будет использоваться как главная страница сайта.
path('store/', include('product.urls', namespace='store')): Определяет маршрут для приложения product по адресу /store/. Включает URL-ы из файла urls.py приложения product и присваивает им пространство имен store, чтобы избежать конфликтов с другими маршрутами.
3. Обслуживание медиафайлов при разработке
if settings.DEBUG: Если проект работает в режиме разработки (DEBUG = True), добавляются маршруты для обслуживания медиафайлов.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT): Добавляет маршруты для медиафайлов, которые хранятся в директории, указанной в settings.MEDIA_ROOT, и доступны по адресу, указанному в settings.MEDIA_URL.
Этот файл конфигурирует пути, обеспечивающие связь между URL-запросами и представлениями в приложении Django, а также поддерживает работу с медиафайлами в режиме разработки.
"""

from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from product.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('store/', include('product.urls', namespace='store')),
    path('user/', include('users.urls', namespace='user')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
