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
  dev_type = models.ForeignKey('Dev_Type', related_name = 'models_dev_type', verbose_name = 'Tipo de Dispositivo', on_delete = models.CASCADE)
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
  description = models.CharField(max_length = 75, verbose_name = 'Dependencia')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.description

  class Meta:
    verbose_name = 'Dependencia'
    verbose_name_plural = 'Dependencias'
    db_table = 'dependencia'
    ordering = ['id']

class Edifice(models.Model):
  edifice = models.CharField(max_length = 50, verbose_name = 'Edificio')
  address = models.TextField(verbose_name = 'Domicilio')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.edifice

  class Meta:
    verbose_name = 'Edificio'
    verbose_name_plural = 'Edificios'
    db_table = 'edificios'
    ordering = ['id']

class Office(models.Model):

  JUJUY = 'JUJUY'
  SALTA = 'SALTA'

  SALTA_CAPITAL = 'SALTA CAPITAL'
  ORAN = 'SAN RAMON DE LA NUEVA ORAN'
  TARTAGAL = 'TARTAGAL'
  SAN_SALVADOR = 'SAN SALVADOR DE JUJUY'

  PROVINCE_CHOICES = [
    (JUJUY, 'JUJUY'),
    (SALTA, 'SALTA'),
  ]

  CITY_CHOICES = {
    JUJUY: [SAN_SALVADOR],
    SALTA: [SALTA_CAPITAL, ORAN, TARTAGAL],
  }

  province = models.CharField(max_length = 50, choices=PROVINCE_CHOICES, default = SALTA, verbose_name = 'Provincia')
  city = models.CharField(max_length = 50, choices = [], default = SALTA_CAPITAL,verbose_name = 'Localidad')
  edifice = models.ForeignKey(Edifice, related_name='office_edifice', verbose_name = 'Edificio', on_delete = models.CASCADE)
  address = models.TextField(verbose_name = 'Domicilio')
  office = models.CharField(max_length = 50, verbose_name = 'Oficina')
  dependency = models.ForeignKey(Dependency, on_delete=models.CASCADE,related_name = 'office_dependency', verbose_name = 'Dependencia')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def save(self, *args, **kwargs):
    self.city = self.CITY_CHOICES.get(self.province, [])[0]
    super().save(*args, **kwargs)

  def __str__(self):
    return f'{self.office} - {self.city}'

  class Meta:
    verbose_name = 'Officina'
    verbose_name_plural = 'Oficinas'
    db_table = 'oficina'
    ordering = ['id']

class Employee(models.Model):
  employee_name = models.CharField(max_length = 50, verbose_name = 'Nombre del Empleado')
  employee_last_name = models.CharField(max_length = 50, verbose_name = 'Apellido')
  cuil = models.CharField(max_length = 11, verbose_name = 'cuil')
  user_pc = models.CharField(max_length = 11, verbose_name = 'Nombre de Usuario')
  office = models.ForeignKey(Office, related_name = 'employee_office', verbose_name = 'Oficina',  on_delete = models.CASCADE,)
  dependency = models.ForeignKey(Dependency, related_name = 'employee_dependency', verbose_name= 'Dependencia',  on_delete = models.CASCADE,)
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.employee_last_name

  def employee_full_name(self):
    return f'{self.employee_last_name}, {self.employee_name}'

  class Meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    db_table = 'empleados'
    ordering = ['id']


class ImgPrinterDevice(models.Model):
  USB = 'USB'
  RED = 'RED'

  CONNECTION_TYPE_CHOICES = [
    (USB, 'USB'),
    (RED, 'RED')
  ]

  ip = models.CharField(max_length = 15, verbose_name = 'Direccion Ip', null = True, blank = True)
  last_review = models.DateField(verbose_name = 'Última Revision')
  connection_type = models.CharField(max_length = 3, choices = CONNECTION_TYPE_CHOICES, default = RED, verbose_name = 'Tipo de Conexion' )
  tech = models.ForeignKey(Techs, related_name = 'img_printer_tech', verbose_name = 'Técnico', on_delete = models.CASCADE)
  model = models.ForeignKey(Model, related_name = 'img_printer_model', verbose_name = 'Modelo', on_delete = models.CASCADE)
  employee = models.ForeignKey(Employee, related_name = 'img_printer_employee', verbose_name = 'Empleado', on_delete = models.CASCADE)
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.model

  def computer_data(self):
    return f'{self.ip}, {self.model}'

  class Meta:
    verbose_name = 'Impresor y Scanner'
    verbose_name_plural = 'Impresoras y Scanners'
    db_table = 'impresoras_scanners'
    ordering = ['id']

class Computer:
  ip = models.CharField(max_length = 15, verbose_name = 'Direccion Ip')
  pc_net_name = models.CharField(max_length = 11, verbose_name = 'Nombre de Equipo en la Red')
  last_review = models.DateField(verbose_name = 'Última Revision')
  tech = models.ForeignKey(Techs, related_name = 'computer_tech', verbose_name = 'Técnico', on_delete = models.CASCADE)
  model = models.ForeignKey(Model, related_name = 'computer_model', verbose_name = 'Modelo', on_delete = models.CASCADE)
  employee = models.ForeignKey(Employee, related_name = 'computer_employee', verbose_name = 'Empleado', on_delete = models.CASCADE)
  printer = models.ManyToManyField(ImgPrinterDevice, related_name='computers', verbose_name='Impresoras')
  date_creation = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de Registro')
  date_updated = models.DateTimeField(auto_now_add = True, verbose_name = 'Última Modificación')

  def __str__(self):
    return self.pc_net_name

  def computer_data(self):
    return f'{self.ip}, {self.pc_net_name}, {self.model}'

  class Meta:
    verbose_name = 'Computadora'
    verbose_name_plural = 'Computadoras'
    db_table = 'computadoras'
    ordering = ['id']