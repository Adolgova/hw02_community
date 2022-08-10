from django.contrib import admin

# Register your models here.

# Из модуля models импортируем модель Post
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
        ) 
    # Добавим возможность изменять группу прямо в списке постов на сайте
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',) 
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    empty_value_display = '-пусто-'
    


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin)  # ранее было: admin.site.register(Post) 

class GroupAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk','title', 'slug', 'description') 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('title',) 
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    empty_value_display = '-пусто-' 

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin

admin.site.register(Group,GroupAdmin)  # ранее было: admin.site.register(Post)