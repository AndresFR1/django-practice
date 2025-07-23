from django.db import models

# modelos de practica

class AutorDb(models.Model):
    nombre = models.CharField(max_length=75, verbose_name="Nombre")
    imagen = models.ImageField(upload_to='autores/', null=True, blank=True, verbose_name="Imagen")
    fecha_de_nacimiento = models.DateField(verbose_name= "Fecha de Nacimiento", null = False, blank = False)
    fecha_fallecimiento = models.DateField(verbose_name="Fecha de Fallecimeinto", null=True, blank=True)
    nacionalidad = models.CharField(max_length=50, verbose_name="Nacionalidad")
    profesion = models.CharField(max_length=50, verbose_name="Profesión")
    
    class Meta:
        db_table = "Autor"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nombre'] 
        
    def __str__(self):
        return self.nombre
    
class Frasedb(models.Model):
    cita = models.TextField(max_length=400, verbose_name="Cita")
    autor_fk = models.ForeignKey(AutorDb, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"
        ordering = ['cita']
        
# modelos

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Eps(models.Model):
    CATEGORY_CHOICES = [
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
    ]
    nombre_eps = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.nombre_eps} ({self.id})"
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    estado = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='activo'
    )
    class Meta:
        verbose_name = ('EPS')
        verbose_name_plural = ('EPS')
        ordering = ['nombre_eps']
    
class FondoPensiones(models.Model):
    CATEGORY_CHOICES = [
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
    ]
    nombre_fondo_pensiones = models.CharField(max_length=40)
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    estado = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='activo'
    )
    class Meta:
        verbose_name = ('Fondo de Pensiones')
        verbose_name_plural = ('Fondos de Pensiones')
        ordering = ['nombre_fondo_pensiones']
    def __str__(self):
        return self.nombre_fondo_pensiones

class FondoCesantias(models.Model):
    CATEGORY_CHOICES = [
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
    ]
    nombre_fondo_cesantias = models.CharField(max_length=40)
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    estado = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='activo'
    )
    def __str__(self):
        return self.nombre_fondo_cesantias
    class Meta:
        verbose_name = ('Fondo de Cesantías')
        verbose_name_plural = ('Fondos de Cesantías')
        ordering = ['nombre_fondo_cesantias']

class Archivos(models.Model):
    nombre_archivo = models.CharField(max_length=40, null=False, blank=False)
    archivo = models.FileField(upload_to='archivos/', null=False, blank=False)
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE, related_name='archivos', null=False, blank=False)
    #id_empleado = models.IntegerField('id_empleado', null=True, blank=True)
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        #return self.({nombre_archivo},{empleado})
        return f'{self.empleado.nombres} {self.empleado.apellidos} Archivo: {self.nombre_archivo}'
    class Meta:
        verbose_name = ('Archivo')
        verbose_name_plural = ('Archivos')
        ordering = ['nombre_archivo']

class Cargo(models.Model):
    CATEGORY_CHOICES = [
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
    ]
    cargo = models.CharField(max_length=40)
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    estado = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='activo'
    )
    def __str__(self):
        return self.cargo
    class Meta:
        verbose_name = ('Cargo')
        verbose_name_plural = ('Cargos')
        ordering = ['cargo']

class Area(models.Model):
    CATEGORY_CHOICES = [
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
    ]

    nombre_area = models.CharField(max_length=40)
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    estado = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='activo'
    )
    def __str__(self):
        return self.nombre_area


class JefeDirecto(models.Model):
    CATEGORY_CHOICES = [
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
    ]

    empleado = models.OneToOneField('Empleado', on_delete=models.PROTECT, related_name='es_jefe_directo',
        null=True,  # Permite nulos para facilitar migraciones y edición
        blank=True
    )
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    estado = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='activo'
    )
    
    class Meta:
        verbose_name = ('Jefe Directo')
        verbose_name_plural = ('Jefes Directos')
        ordering = ['empleado']

    def __str__(self):
        if self.empleado:
            return f'Jefe: {self.empleado.nombres} {self.empleado.apellidos} (ID: {self.empleado.id})'
        return 'Jefe sin empleado asignado'

class Empleado(models.Model):
    CATEGORY_CHOICES_TIPO_DOCUMENTO = [
    ('cc', 'CC'),
    ('ti', 'TI'),
    ('ppt', 'PPT'),
    ('ce', 'CE'),
    ]
    CATEGORY_CHOICES_SEXO = [
    ('masculino', 'Masculino'),
    ('femenino', 'Femenino'),
    ]
    CATEGORY_CHOICES_RH = [
    ('a+', 'A+'),
    ('a-', 'A-'),
    ('b+', 'B+'),
    ('ab+', 'AB+'),
    ('ab-', 'AB-'),
    ('o+', 'O+'),
    ('o-', 'O-'),
    ]
    CATEGORY_CHOICES_ESTADO_CIVIL = [
    ('soltero', 'SOLTERO/A'),
    ('union_libre', 'UNIÓN LIBRE'),
    ('casado', 'CASADO/A'),
    ('divorciado', 'DIVORCIADO/A'),
    ]
    CATEGORY_CHOICES_MOTIVO_RETIRO = [
    ('voluntario', 'VOLUNTARIO'),
    ('terminacion_de_contrato', 'TERMINO DE CONTRATO'),
    ('periodo_de_prueba', 'PERIODO DE PRUEBA'),
    ('abandono_de_cargo', 'ABANDONO DE CARGO'),
    ('no_aplica', 'NO APLICA'),
    ]
    CATEGORY_CHOICES_TIPO_CONTRATO = [
    ('obra_labor', 'OBRA LABOR'),
    ('indefinido', 'INDEFINIDO'),
    ('fijo', 'FIJO'),
    ('aprendizaje', 'APRENDIZAJE'),
    ]
    CATEGORY_CHOICES_ESTADO = [
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
    ]
    
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    tipo_documento = models.CharField(max_length=10, choices=CATEGORY_CHOICES_TIPO_DOCUMENTO, default='cc')
    numero_documento = models.CharField(max_length=15)
    lugar_expedicion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    numero_celular = models.CharField(max_length=13)
    numero_whatsapp = models.CharField(max_length=13)
    correo_electronico = models.CharField(max_length=120)
    direccion_residencia = models.CharField(max_length=255)
    localidad_residencia = models.CharField(max_length=50)
    barrio_residencia = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, choices=CATEGORY_CHOICES_SEXO, default='masculino')
    rh = models.CharField(max_length=3, choices=CATEGORY_CHOICES_RH, default='a+')
    estado_civil = models.CharField(max_length=15, choices=CATEGORY_CHOICES_ESTADO_CIVIL, default='soltero/a')
    trabajo_previo_empresa = models.BooleanField()
    motivo_retiro = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES_MOTIVO_RETIRO,
        default='voluntario'
    )

    def clean(self):
        if self.trabajo_previo_empresa == False:
            self.motivo_retiro = 'no_aplica'
        elif self.motivo_retiro == 'no_aplica':
            raise ValidationError({'motivo_retiro': 'Debe seleccionar un motivo si ha trabajado previamente.'})
        super().clean()
        
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    tipo_contrato = models.CharField(max_length=20, choices=CATEGORY_CHOICES_TIPO_CONTRATO, default='obra_labor')
    sueldo = models.CharField(max_length=10)
    fecha_ingreso = models.DateField()
    jefe_directo = models.ForeignKey(
    JefeDirecto,
    on_delete=models.PROTECT,
    null=True,
    blank=True,
    related_name='empleados_a_cargo'
    )
    parentesco_familiar = models.CharField(max_length=20)
    nombre_completo_familiar = models.CharField(max_length=120)
    numero_celular_familiar = models.CharField(max_length=13)
    eps = models.ForeignKey(Eps, on_delete=models.PROTECT)
    fondo_pensiones = models.ForeignKey(FondoPensiones, on_delete=models.PROTECT)
    fondo_cesantias = models.ForeignKey(FondoCesantias, on_delete=models.PROTECT)
    estado = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES_ESTADO,
        default='activo'
    )
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
    class Meta:
        verbose_name = ('Empleado')
        verbose_name_plural = ('Empleados')
        ordering = ['nombres', 'apellidos']

class Hijo(models.Model):
    nombre_completo_hijo = models.CharField(max_length=70)
    fecha_nacimiento_hijo = models.DateField()
    sexo = models.CharField(max_length=10)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre_completo_hijo
    class Meta:
        verbose_name = ('Hijo')
        verbose_name_plural = ('Hijos')
        ordering = ['nombre_completo_hijo']
    
    
class Educacion(models.Model):
    CATEGORY_CHOICES_NIVEL_ACADEMICO = [
    ('bachiller', 'BACHILLER'),
    ('tecnico', 'TÉCNICO'),
    ('tecnologo', 'TECNÓLOGO'),
    ('profesional', 'PROFESIONAL'),
    ('postgrado', 'POSTGRADO'),
    ]
    CATEGORY_CHOICES_ESTUDIA_ACTUALMENTE = [
    ('si', 'Si'),
    ('no', 'No'),
    ]
    CATEGORY_CHOICES_JORNADA = [
    ('diurno', 'DIURNO'),
    ('nocturno', 'NOCTURNO'),
    ('virtual', 'VIRTUAL'),
    ('fin_de_semana', 'FIN DE SEMANA'),
    ('no_aplica', 'NO APLICA'),
    ]
    nivel_academico = models.CharField(max_length=40, choices=CATEGORY_CHOICES_NIVEL_ACADEMICO, default='bachiller')
    anio_finalizacion = models.DateField()
    estudia_actualmente = models.CharField( max_length=2, choices=CATEGORY_CHOICES_ESTUDIA_ACTUALMENTE, default='no')
    titulo = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    jornada = models.CharField(max_length=20, choices=CATEGORY_CHOICES_JORNADA, default='diurno')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.nivel_academico} - {self.titulo}'
    class Meta:
        verbose_name = ('Educación')
        verbose_name_plural = ('Educaciones')
        ordering = ['nivel_academico', 'titulo']

class UsuariosDePlataformas(models.Model):
    usuario_plataforma_1 = models.CharField(max_length=50, null= True, blank= True)
    usuario_plataforma_2 = models.CharField(max_length=50, null= True, blank= True)
    usuario_plataforma_3 = models.CharField(max_length=50, null= True, blank= True)
    usuario_plataforma_4 = models.CharField(max_length=50, null= True, blank= True)
    usuario_plataforma_5 = models.CharField(max_length=50, null= True, blank= True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Usuarios plataformas - Empleado {self.empleado.id}'
    class Meta:
        verbose_name = ('Usuarios de Plataformas')
        verbose_name_plural = ('Usuarios de Plataformas')
        ordering = ['empleado']
