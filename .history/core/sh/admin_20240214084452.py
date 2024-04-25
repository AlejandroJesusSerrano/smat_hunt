from django.contrib import admin
from core.sh.models import *
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