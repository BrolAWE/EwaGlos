from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Section)
admin.site.register(Subsection)
admin.site.register(Word)
admin.site.register(WordTranslation)
admin.site.register(SectionTranslation)
admin.site.register(SubsectionTranslation)