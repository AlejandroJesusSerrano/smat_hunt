from django.db import models
from datetime import datetime

# Create your models here.
class Brand(models.Model):
  brand = models.CharField(max_length=50, verbose_name = 'Marca')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Regilstro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.brand

  class Meta:
    verbose_name = 'Marca'
    verbose_name_plural = 'Marcas'
    db_table = 'marca'
    ordering = ['id']

class Dev_Type(models.Model):
  dev_type = models.CharField(max_length = 50, verbose_name = 'Tipo de Dispositivo')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Regilstro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.dev_type

  class Meta:
    verbose_name = 'Tipo de Dispositivo'
    verbose_name_plural = 'Tipos de Dispositivo'
    db_table = 'tipo_de_dispositivo'
    ordering = ['id']

class Model(models.Model):
  dev_type = models.ForeignKey('Dev_Type', related_name = 'models_dev_type', on_delete = models.CASCADE)
  brand = models.ForeignKey('Brand', related_name = 'models_brand', on_delete = models.CASCADE)
  model = models.CharField(max_length = 50, verbose_name = 'Modelo')
  image = models.ImageField(upload_to='img_models/%Y/%m/%d', null = True, blank = True, verbose_name = 'Imagen')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.model

  class Meta:
    verbose_name = 'Modelo'
    verbose_name_plural = 'Modelos'
    db_table = 'modelo'
    ordering = ['id']

class Techs(models.Model):
  name = models.CharField(max_length = 75, verbose_name = 'Nombre')
  last_name = models.CharField(max_length = 75, verbose_name = 'Apellido')

  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Tecnico'
    verbose_name_plural = 'Tecnicos'
    db_table = 'tecnico'
    ordering = ['id']

class Dependency(models.Model):
  description = models.Charfield(max_length = 75, verbose_name = 'Dependencia')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.description

  class Meta:
    verbose_name = 'Dependencia'
    verbose_name_plural = 'Dependencias'
    db_table = 'dependencia'
    ordering = ['id']

class Office(models.Model):
  province = models.CharField(max_length = 50, verbose_name = 'Provincia')
  city = models.CharField(max_length = 50, verbose_name = 'Localidad')
  edifice = models.CharField(max_length = 75, verbose_name = 'edificio')
  address = models.TextField(verbose_name = 'Domicilio')
  office = models.CharField(max_length = 50, verbose_name = 'Oficina')
  dependency = models.ForeignKey(Dependency, on_delete=models.CASCADE, verbose_name = 'Dependencia')

  def __str__(self):
    return self.office

  class Meta:
    verbose_name = 'Officina'
    verbose_name_plural = 'Oficinas'
    db_table = 'oficina'
    ordering = ['id']