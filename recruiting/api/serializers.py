from rest_framework import serializers

from recruiting.models import Company, City, VacancyImage
from .. import models


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Company
        fields = ('name', 'location')


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.City
        fields = ('name',)


class VacancyImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.VacancyImage
        fields = ('url',)


class VacancySerializer(serializers.ModelSerializer):
    location = CitySerializer(many=True)
    company = CompanySerializer()
    image_list = VacancyImageSerializer(many=True)

    class Meta:
        model = models.Vacancy
        fields = ('is_active', 'title', 'location',
                  'starts_at', 'ends_at', 'description',
                  'image_list', 'company')

    def update(self, instance, validated_data):
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.title = validated_data.get('title', instance.title)

        instance.locations.clear()
        locations = validated_data.get('location')
        for loc in locations:
            city = loc.get('name')
            if not City.objects.filter(name=city):
                c = City.objects.create(name=city)
                instance.location.add(c)
            else:
                instance.location.add(City.objects.filter(name=city)[0])

        instance.starts_at = validated_data.get('starts_at', instance.starts_at)
        instance.ends_at = validated_data.get('ends_at', instance.ends_at)
        instance.description = validated_data.get('description', instance.description)

        instance.image_list.clear()
        images = validated_data.get('image_list')
        for img in images:
            image = img.get('url')
            if not VacancyImage.objects.filter(url=image):
                i = VacancyImage.objects.create(url=image)
                instance.image_list.add(i)
            else:
                instance.image_list.add(VacancyImage.objects.filter(url=image)[0])

        c = Company.objects.filter(name=instance.company.name)[0]
        c.name = validated_data.get('company').get('name')
        c.location = validated_data.get('company').get('location')
        c.save()
        instance.company = c
        instance.save()
        return instance
