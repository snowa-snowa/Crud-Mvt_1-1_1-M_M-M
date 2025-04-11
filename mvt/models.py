from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Passport(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=20)

    def __str__(self):
        return f'u chelaveka {self.person.first_name} yest id {self.passport_number}'


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'Reporter: {self.first_name}'


class Article(models.Model):
    headline = models.CharField(max_length=100)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return f'Statya: {self.headline} by {self.reporter.first_name}'


class Fuel(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    fuels = models.ManyToManyField(Fuel, related_name='cars')

    def __str__(self):
        return self.name
