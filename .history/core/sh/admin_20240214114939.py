from typing import Any, Mapping
from django import forms
from django.contrib import admin
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from core.sh.models import *

class OfficeForm(forms.ModelForm):
  class Meta:
    model = Office
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    instance = getattr(self, 'instance', None)
    if instance and instance.province:
      self.fields['city'].choices = [(c, c) for c in instance.CITY_CHOICES.get(instance.province, [])]
      
class OfficeAdmin(admin.ModelAdmin):
  form= OfficeForm

admin.site.register(Office, OfficeAdmin)



# Register your models here.
# Equipos
admin.site.register(Brand)
admin.site.register(Dev_Type)
admin.site.register(Model)
admin.site.register(ImgPrinterDevice)
admin.site.register(Computer)

# tecnicos
admin.site.register(Techs)

# Dependencias y oficinas
admin.site.register(Dependency)
admin.site.register(Edifice)
admin.site.register(Office)

# Empleados -usuarios de equipos-
admin.site.register(Employee)