from django.contrib import admin

# Register your models here.
from django.forms import TextInput, Textarea

from core.models import *


class SectionTranslationInline(admin.TabularInline):
    model = SectionTranslation
    raw_id_fields = ("section",)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("code",)
    inlines = [
        SectionTranslationInline,
    ]


class SubsectionTranslationInline(admin.TabularInline):
    model = SubsectionTranslation
    raw_id_fields = ("subsection",)


@admin.register(Subsection)
class SubsectionAdmin(admin.ModelAdmin):
    list_display = ("code",)
    inlines = [
        SubsectionTranslationInline,
    ]


class WordTranslationInline(admin.TabularInline):
    model = WordTranslation
    raw_id_fields = ("word",)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '13'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 12, 'cols': 37})},
    }


class CloseSenseWordInline(admin.TabularInline):
    model = CloseSenseWord
    raw_id_fields = ("word",)
    fk_name = "word"




@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("code",)
    inlines = [
        WordTranslationInline,
        CloseSenseWordInline,
    ]
