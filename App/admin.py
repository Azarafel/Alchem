from django.contrib import admin

from django.contrib import admin

from App.models import Ingredients, Equipment, Replacement, Likes, Cocktail

@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    pass


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    pass

@admin.register(Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    pass

@admin.register(Cocktail)
class CocktailAdmin(admin.ModelAdmin):
    pass