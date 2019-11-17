from django.contrib import admin

# Register your models here.
from core.models import *


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Subsection)
class SubsectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(WordTranslation)
class WordTranslationAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(SectionTranslation)
class SectionTranslationAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(SubsectionTranslation)
class SubsectionTranslationAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(CloseSenseWord)
class CloseSenseWordAdmin(admin.ModelAdmin):
    list_display = ("word", "close_sense")
