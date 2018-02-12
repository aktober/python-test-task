from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name


class VacancyImage(models.Model):
    url = models.URLField(blank=True, null=True)


class Vacancy(models.Model):
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=256)
    location = models.ManyToManyField(City)
    starts_at = models.CharField(max_length=20)
    ends_at = models.CharField(max_length=20)
    description = models.TextField()
    image_list = models.ManyToManyField(VacancyImage)
    company = models.ForeignKey(Company)

    class Meta:
        verbose_name_plural = "vacancies"

    def __str__(self):
        return self.title
