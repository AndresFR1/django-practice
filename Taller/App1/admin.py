from django.contrib import admin
from .models import AutorDb, Frasedb
# Register your models here.

# class Frese_in_line(admin.TabularInline):
#     model = Frasedb
#     extra = 1

# class AutorDbAdmin(admin.ModelAdmin): 
#     fields = ('imagen','nombre', 'fecha_de_nacimiento', 'fecha_fallecimiento', 'nacionalidad', 'profesion')
#     list_display = ('nombre', 'fecha_de_nacimiento', 'fecha_fallecimiento', 'nacionalidad', 'profesion')
    
#     inlines = [Frese_in_line]
    
#     def actualizar_a(self, request, queryset):
#         for i in queryset:
#             if "a" in i.nombre:
#                 i.nombre = i.nombre.replace("a", "A")
#                 i.save()
#         self.message_user(request, "Actualización completada")
#     actualizar_a.short_description = "Actualizar nombres que contienen 'a' a 'A'"
#     actions = ["actualizar_a"]

    
# admin.site.register(AutorDb, AutorDbAdmin)


# @admin.register(Frasedb)
# class FrasedbAdmin(admin.ModelAdmin):
#     fields = ('cita', 'autor_fk')
#     list_display = ('cita', 'autor_fk')
    
# from django.contrib import admin
# from .models import (
#     Eps,
#     FondoPensiones,
#     FondoCesantias,
#     Archivos,
#     Cargo,
#     Area,
#     JefeDirecto,
#     Empleado,
#     Hijo,
#     Educacion,
#     UsuariosDePlataformas
# )

# Utilidad común para mostrar campos base
from django.contrib import admin
from .models import (
    Eps,
    FondoPensiones,
    FondoCesantias,
    Archivos,
    Cargo,
    Area,
    JefeDirecto,
    Empleado,
    Hijo,
    Educacion,
    UsuariosDePlataformas,
)

# # Reutilizable para modelos con timestamps
# class TimeStampedAdmin(admin.ModelAdmin):
#     readonly_fields = ('creado', 'modificado')
#     ordering = ('-creado',)

# # Para modelos con activo + timestamps
# class ActivableAdmin(TimeStampedAdmin):
#     list_display = ('__str__', 'creado', 'modificado')
#     list_filter = ('activo',)
#     search_fields = ('nombre_area',)  # ajusta este campo según el modelo

# Register EPS
@admin.register(Eps)
class EpsAdmin(admin.ModelAdmin):
    list_display = ('nombre_eps', 'creado', 'modificado')
    search_fields = ('nombre_eps',)
    

# Register FondoPensiones
@admin.register(FondoPensiones)
class FondoPensionesAdmin(admin.ModelAdmin):
    list_display = ('nombre_fondo_pensiones', 'creado', 'modificado')
    search_fields = ('nombre_fondo_pensiones',)

# Register FondoCesantias
@admin.register(FondoCesantias)
class FondoCesantiasAdmin(admin.ModelAdmin):
    list_display = ('nombre_fondo_cesantias', 'creado', 'modificado')
    search_fields = ('nombre_fondo_cesantias',)

class ArchivosInline(admin.TabularInline):
    model = Archivos
    extra = 0
    fields = ('nombre_archivo', 'archivo', 'creado', 'modificado')
    readonly_fields = ('creado', 'modificado')

# Register Archivos
@admin.register(Archivos)
class ArchivosAdmin(admin.ModelAdmin):
    list_display = ('nombre_archivo', 'creado', 'modificado', 'empleado')
    search_fields = ('nombre_archivo',)
    
# Register Cargo
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'creado', 'modificado')
    search_fields = ('cargo',)

# Register Area (usa Admin con activo)
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre_area', 'creado', 'modificado')
    search_fields = ('nombre_area',)

# Register JefeDirecto
@admin.register(JefeDirecto)
class JefeDirectoAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'creado', 'modificado', )
    search_fields = ('empleado',)
    
# Register Empleado (usa Admin con activo)
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'creado', 'modificado', 'estado')
    search_fields = ('nombres', 'apellidos', 'numero_documento')
    list_filter = ('area', 'cargo')
    inlines = [ArchivosInline]
    
# Register Hijo
@admin.register(Hijo)
class HijoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo_hijo', 'empleado', 'creado', 'modificado')
    search_fields = ('nombre_completo_hijo',)

# Register Educacion
@admin.register(Educacion)
class EducacionAdmin(admin.ModelAdmin):
    list_display = ('nivel_academico', 'titulo', 'empleado', 'creado', 'modificado')
    search_fields = ('titulo', 'nivel_academico')

# Register UsuariosDePlataformas
@admin.register(UsuariosDePlataformas)
class UsuariosPlataformasAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'creado', 'modificado')
