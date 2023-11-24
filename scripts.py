import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Mark, Chastisement, Commendation, Lesson
def create_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        return schoolkid
    except ObjectDoesNotExist:
        print('Такого ученика не существует. Повторите ввод.')
    except MultipleObjectsReturned:
        print('Учеников с таким именем несколько. Уточните ввод.')
def fix_marks(child):
        marks = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
        for mark in marks:
            assessment = 5
            mark.points = assessment
            mark.save()
def remove_chastisements(child):
        chastisement = Chastisement.objects.filter(schoolkid=child)
        chastisement.delete()
def create_commendation(child, subject):
        text_commendation = ['Молодец!', 'Отлично!', 'Хорошо!', 'Великолепно!',
                             'Прекрасно!', 'Очень хороший ответ!', 'Талантливо!',
                             'Уже существенно лучше!', 'Так держать!',
                             'Ты на верном пути!', 'Здорово!',
                             'Это как раз то, что нужно!', 'Я тобой горжусь!',
                             'С каждым разом у тебя получается всё лучше!']
        random_text = random.choice(text_commendation)
        lessons = Lesson.objects.filter(
                     year_of_study=child.year_of_study,
                     group_letter=child.group_letter,
                     subject__title=subject
        )
        if not lessons:
            return print('Такого предмета не существует. Повторите ввод.')
        lesson = lessons.order_by('-date').first()
        Commendation.objects.create(
            schoolkid=child,
            created=lesson.date,
            subject=lesson.subject,
            teacher=lesson.teacher,
            text=random_text
        )

