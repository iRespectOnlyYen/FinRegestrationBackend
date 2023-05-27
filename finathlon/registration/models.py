from django.db import models
from django.utils.text import slugify


class Role(models.Model):
    title = models.CharField("Роль", max_length=50)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.url:  # Генерируем значение поля url только при его отсутствии
            self.url = slugify(self.title)
        super().save(*args, **kwargs)


class User(models.Model):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    patronymic = models.CharField("Отчество", max_length=100)
    birth_date = models.DateField("Дата рождения")
    birth_place = models.CharField("Место рождения", max_length=100)
    live_place = models.CharField("Место жительства", max_length=100)
    index_place = models.IntegerField("Индекс места жительства")
    phone_number = models.IntegerField()
    role = models.ForeignKey(Role, verbose_name="Роль", on_delete=models.SET_NULL, null=True)


class Teacher(models.Model):
    POSITION_TYPES = (
        ('full-time', 'Полная занятость'),
        ('part-time', 'Частичная занятость'),
    )
    EDUCATION_TYPE = (
        ('bac', "Бакалавр"),
        ('mag', "Магистр"),
        ('spec', "Специалист"),
        ('cand_science', "Кандидат наук"),
        ('dr_scince', "Доктор наук"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    organization = models.CharField("Название организации", max_length=200)
    post = models.CharField("Должность", max_length=150)
    position_type = models.CharField("Тип занятости", max_length=100, choices=POSITION_TYPES)
    post_index = models.IntegerField("Почтовый индекс")
    work_sector = models.CharField("Отрасль", max_length=200)
    start_year = models.SmallIntegerField("Год начала работы")

    university_title = models.CharField("Название ВУЗа", max_length=200)
    end_year = models.SmallIntegerField("Год окончания ВУЗа")
    rank = models.CharField("Специальность", max_length=150)
    education_type = models.CharField("Степень", max_length=100, choices=EDUCATION_TYPE)


class SchoolBoy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    school_index = models.IntegerField("Индекс школы")
    title = models.CharField("Название школы", max_length=200)
    class_level = models.SlugField()
    orphan_status = models.BooleanField("Статус сироты")
    disability = models.BooleanField("Являюсь лицом с ограниченными возможностями")


class Team(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teams')
    students = models.ManyToManyField(SchoolBoy, related_name='teams')
