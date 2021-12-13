from django.db import models

from usersregistration.choices import SCHOOL_POSITIONS

class Person(models.Model):
    photo = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    rg = models.CharField(max_length=14)
    cep = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    birth_date = models.DateField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    class Meta:
        abstract = True


class SchoolEmployee(Person):
    training_area = models.CharField(max_length=100)
    position_at_school = models.CharField(max_length=2, choices=SCHOOL_POSITIONS)
    ctps = models.CharField(max_length=25)
    wage = models.DecimalField(max_digits=15, decimal_places=2)
    hiring_date = models.DateField()

    def __str__(self) -> str:
        return self.name

class Student(Person):
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name