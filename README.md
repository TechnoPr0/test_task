Приложение для работы с базой данных для тестового задания в компанию "ПТМК".

```bash
#Создание таблицы "employees"
python main.py 1

#Создание строки с ФИО, датой рождения и полом (Формат даты ГГГГ-ММ-ДД).
python main.py 2 "Petrov Ivan Olegovich" 1980-12-25 Male

#Отображение таблицы "employees"
python main.py 3

#При запуске с пустой таблицой генерирует 100000 записей сотрудников примерно напополам женского и мужского пола.
#При запуске с таблицой в которой имеются записи генерирует в 1000 раз меньше записей с фамилиями начинающимися на "F"
python main.py 4

#Фильтрует записи по первой букве имени (в данном примере 'F'), также выводит количество записей и время потраченное на выполнение выборки.
python main.py 5

#Удаляет таблицу из бд
python main.py 0
```

В этой выборке мне не удалось выявить изменений в скорости выполнения программы, пробовал добавлять индекс к полю 'full_name' для ускоренного вывода таблицы, так-же пробовал добавить метод yeld_per() для извлечения данных порциями.
Все эти действия не имели эффекта скорость извлечения строк с первой буквой "F" была в диапозоне 1100 - 1400 микросекунд. Величина таблицы 14000000 строк, начинающихся с буквы "F" - 3430769.

Возможно разницы во времени нет из-за того, что тесты проводились в SQLite, но к сожалению не хватило времени на развёртывание PostgreSQL.
