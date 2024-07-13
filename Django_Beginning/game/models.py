from django.db import models
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy  # импортируем «ленивый» геттекст с подсказкой

class Games(models.Model):
    name = models.CharField(
        default='NoName',
        max_length=64,
        verbose_name='name of game'
    )

# Пример ArrayField только в PostgreSQL вы можете «нативно», прямо в базе данных хранить массивы
# from django.contrib.postgres.fields import ArrayField
#
# class User(models.Model):
#     pseudonyms = ArrayField(
#         models.CharField(max_length=10, blank=True),
#         size=8,
#     )
"""
первый параметр этого поля — поле, которое будет полем массива, а второй — размер этого массива; таким образом, 
в нашем примере pseudonyms — это массив из восьми полей типа varchar(10). 
При использовании ArrayField вы можете использовать оператор __contains для поиска значений в массиве 
(он использует специфический для Postgres оператор @>
"""

# JSONField это хранение JSON прямо в БД.
# from django.contrib.postgres.fields import JSONField
#
# class User(models.Model):
#     name = models.CharField(max_length=200)
#     profile_data = JSONField(null=True)
"""
По этому полю можно осуществлять фильтрацию средствами БД. ORM.
__contains для точной проверки наличия пар «ключ-значение»
__contained_by для проверки наличия одной из перечисленных пар
>>> User.objects.create(name='Dmitry', data={
...     'country': 'Russia',
...     'children': [
...         {
...             'name': 'John',
...         },
...     ]
... })
<User: Dmitry>
>>> User.objects.create(name='Megan Fox', data={'country': 'UK', 'children': None})
<User: Megan Fox>
>>> User.objects.filter(data__country='UK')
<QuerySet [<User: Megan Fox>]>
"""
# RangeField Это поля, хранящие числовой интервал, то есть «отрезок на числовой прямой»
"""
Они существуют в следующих вариантах (по варианту на каждый доступный подтип): 
IntegerRangeField, BigIntegerRangeField, DecimalRangeField, DateTimeRangeField и DateRangeField
Эти поля поддерживают следующие особенные операторы:

__contains для проверки, содержится ли конкретное значение в интервале;
__contained_by для проверки, содержится ли этот интервал в другом (также можно использовать с 
числовыми полями для проверки, находятся ли они в интервале);
__overlap для проверки пересечения интервалов.
"""

class Category(models.Model):
    name = models.CharField(max_length=100,
                            help_text=gettext_lazy('category name'))  # добавим переводящийся текст подсказку к полю


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    kind = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='kinds',
        verbose_name=gettext_lazy('help text for MyModel model', 'This is the help text'),
    )