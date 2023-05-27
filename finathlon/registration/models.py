from django.db import models


class Person(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    residence_index = models.CharField(max_length=10)
    residence_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    additional_json_data = models.CharField(max_length=255)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name
