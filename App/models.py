from django.db import models
from django.contrib.auth.models import User


class Ingredients(models.Model):
    name = models.CharField(max_length=48)


class Equipment(models.Model):
    name = models.CharField(max_length=48)


class Cocktail(models.Model):
    name = models.CharField(max_length=48)
    description = models.CharField(max_length=128)
    equipment = models.ManyToManyField(Equipment)
    ingredients = models.ManyToManyField(Ingredients)
    alcohol = models.BooleanField()


class Replacement(models.Model):
    class Meta:
        unique_together = (('id_cocktail', 'id_ingredient', 'id_replacement'),)
    id_cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    id_ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE, related_name="ingredient")
    id_replacement = models.ForeignKey(Ingredients, on_delete=models.CASCADE, related_name="replacement")


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    like = models.BooleanField(default=None)