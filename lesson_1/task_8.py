"""
Задание 8.	Определить, является ли год, который ввел пользователем,
високосным или не високосным.

Подсказка:
Год является високосным в двух случаях: либо он кратен 4,
но при этом не кратен 100, либо кратен 400.

Попробуйте решить задачу двумя способами:
1. Обычное ветвление
2. Тернарный оператор

П.С. - Тернарные операторы, также известные как условные выражения,
представляют собой операторы, которые оценивают что-либо на основе условия,
являющегося истинным или ложным. Он был добавлен в Python в версии 2.5 .
Он просто позволяет протестировать условие в одной строке,
заменяя многострочное if-else, делая код компактным.
"""

USER_YEAR = int(input('Введите год: '))

if (USER_YEAR % 4 == 0 and USER_YEAR % 100 != 0) or USER_YEAR % 400 == 0:
    print('Високосный')
else:
    print('Не високосный')

res = 'Високосный' if (USER_YEAR % 4 == 0 and USER_YEAR % 100 != 0) or USER_YEAR % 400 == 0 else 'Не високосный'
print(res)
