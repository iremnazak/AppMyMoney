from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
  pass
#   class Media: Şekil şukul
#       js = (
#            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#            'modeltranslation/js/tabbed_translation_fields.js',
#        )
#       css = {
#          'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#     }

@admin.register(Brand)
class ProductAdmin(TranslationAdmin):
   pass

@admin.register(Gender)
class ProductAdmin(TranslationAdmin):
   pass

@admin.register(Color)
class ProductAdmin(TranslationAdmin):
   pass

@admin.register(CaseShape)
class ProductAdmin(TranslationAdmin):
   pass

@admin.register(StrapType)
class ProductAdmin(TranslationAdmin):
   pass

@admin.register(GlassFeature)
class ProductAdmin(TranslationAdmin):
   pass

@admin.register(Style)
class ProductAdmin(TranslationAdmin):
   pass

@admin.register(Mechanism)
class ProductAdmin(TranslationAdmin):
   pass
