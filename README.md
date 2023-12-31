# Скрипт для корректировки значений в электронном дневнике школы

Скрипт создан для исправления оценок, удаления замечаний и создания положительных похвал.


## Запуск

- Скачайте скрипт
- Убедитесь, что сервер с электронным дневником запущен. Если работаете локально, то:
  * Создайте БД командой `python3 manage.py migrate`
  * Запустите сервер командой `python3 manage.py runserver`
- Запустите шелл командой `python3 manage.py shell`
- Откройте скрипт в любом текстовом редакторе. Уберите все пустые строки из скрипта. Скопируйте полностью внутреннее содержание скрипта в `shell`.

## Описание функций

`create_schoolkid` - создание модели ученика. 
Создайте модель ученика для которого хотите внести исправления, использую его фамилию и имя.  

![Создание](https://github.com/univernik77/e-diary-only-script/assets/146747152/f308b753-fb3d-4696-8ed2-80be661a3693)  

`fix_marks` - исправление всех оценок ниже 4 на 5.
Для исправления оценок запустите функцию, которая в качестве аргумента принимает модель ученика.  

![Снимок экрана от 2023-11-24 13-17-12](https://github.com/univernik77/e-diary-only-script/assets/146747152/acdbc894-e519-4e12-92dd-a68014ed65c3)  

Результат выполнения функции. До:  

![Оценки до](https://github.com/univernik77/e-diary-only-script/assets/146747152/55f3ecf5-9d05-4da3-86c8-71e908c09a01)  

После:  

![Оценки после](https://github.com/univernik77/e-diary-only-script/assets/146747152/58f057b0-dbe7-4f20-bc81-4278a6c954fb)  

`remove_chastisements` - удаление замечаний
Для удаления замечаний запустите функцию, которая в качестве аргумента принимает модель ученика.  

![Снимок экрана от 2023-11-24 13-19-21](https://github.com/univernik77/e-diary-only-script/assets/146747152/5cf2d247-f9b9-4af3-b4a4-31bd9c878021)  

Результат выполнения функции. До:  

![Замечания](https://github.com/univernik77/e-diary-only-script/assets/146747152/bb17f976-49c8-442a-8209-26041d6d8db6)  

После выполнения функции все замечания удалены.  

`create_commendation` - создание похвалы
Для удаления замечаний запустите функцию, которая в качестве аргумента принимает модель ученика,школьный предмет и тексты для хвалы.  

![Снимок экрана от 2023-11-25 14-45-00](https://github.com/univernik77/e-diary-only-script/assets/146747152/d28e9528-4f4f-4089-b5da-7ac8e90fde7d)


Результат выполнения функции.  

![Хвала](https://github.com/univernik77/e-diary-only-script/assets/146747152/1b16e4e9-7ec3-42bc-9232-05a0881d8c94)


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
