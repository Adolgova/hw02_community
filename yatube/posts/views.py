# до пункта 17.6 было так:
#from django.http import HttpResponse
#from django.shortcuts import render
# Импортируем модель, чтобы обратиться к ней
#def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    #template = 'posts/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    #title = 'Yatube'
    # Словарь с данными принято называть context
    #context = {
        # В словарь можно передать переменную
        #'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        #'text': 'Это главная страница проекта Yatube',
    #}
    # Третьим параметром передаём словарь context
    #return render(request, template, context) 
# В урл мы ждем параметр, и нужно его прередать в функцию для использования
#def group_list(request):
#    template = 'posts/group_list.html'
#    title = 'Группы Yatube'
#    context = {
#        # В словарь можно передать переменную
#        'title': title,
#        # А можно сразу записать значение в словарь. Но обычно так не делают
#        'text': 'Здесь будет информация о группах проекта Yatube',
#    }
#    return render(request, template, context)

from django.http import HttpResponse   
from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, template, context) 


# В урл мы ждем параметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    template = 'posts/group_list.html'
    
    # Функция get_object_or_404 получает по заданным критериям объект 
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug = slug)
    
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)