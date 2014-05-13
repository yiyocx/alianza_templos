# -*- coding: utf-8 -*-
from django.db import models
from djgeojson.fields import PointField


class Proyecto(models.Model):
	"""
	Representacion de un Proyecto de construccion 
	de un templo para una iglesia de la IACYMC
	"""
	nombre = models.CharField(max_length=40)
	direccion = models.TextField()
	

	coordenadas = PointField()
	
	TIPO_OWNER_ESCRITURA_CHOICES = (
		(0, 'Partner Organization'),
		(1, 'Congregacion'),
		(2, 'Lideres de la Iglesia'),
		(3, 'Otro'),
	)
	owner_escritura = models.SmallIntegerField()
	TIPO_ADQUISICION_CHOICES = (
		(0, 'Comprado'),
		(1, 'Donado'),
	)
	tipo_adquisicion = models.SmallIntegerField()

	""" Informacion de la comunidad """
	poblacion_comunidad = models.CharField(max_length=40)
	nombre_comunidad = models.CharField(max_length=50)
	region = models.CharField(max_length=30) # Tambien puede ser estado, region o distrito
	pais = models.CharField(max_length=20)

	ciudad_cercana = models.CharField(max_length=30)
	distancia_ciudad_cercana = models.PositiveSmallIntegerField() # En km
	iglesia_cercana = models.CharField(max_length=30)
	distancia_iglesia_cercana = models.PositiveSmallIntegerField() # En km

	""" Informacion de la congregacion """
	lengua_primaria = models.CharField(max_length=20)
	fecha_fundacion = models.DateField()
	ingresos_ofrendas = models.DecimalField(max_digits=15, decimal_places=3) # ¿Unidad del dinero? Mensual
	cant_asistentes_adultos = models.SmallIntegerField()
	cant_asistentes_ninos = models.SmallIntegerField()
	cant_miembros_adultos = models.SmallIntegerField()
	cant_miembtos_ninos = models.SmallIntegerField()

	""" Informacion del pastor """
	nombre_pastor = models.CharField(max_length=50)
	entrenamiento_biblico = models.CharField(max_length=50)
	titulos_obtenidos = models.CharField(max_length=50)
	anios_en_actual_iglesia = models.PositiveSmallIntegerField()
	anios_en_ministerio = models.PositiveSmallIntegerField()
	ESTADO_CIVIL_CHOICES = (
		(0, 'Soltero'),
		(1, 'Casado'),
	)
	estado_civil = models.SmallIntegerField()
	cantidad_hijos = models.PositiveSmallIntegerField()
	# Se debe almacenar una foto del pastor
	q1_disponibilidad_material_estudio_biblico = models.BooleanField() # ¿El pastor ha hablado de la disponibilidad de material para estudio biblico?
	q1_why_not = models.TextField()
	q2_usa_material_crecimiento_iglesia = models.BooleanField() # ¿El pastor ha acordado usar este material para crecimiento de la iglesia?
	q2_why_not = models.TextField()
	q2_how_do = models.TextField()

	""" Informacion de construccion """
	tiempo_terminar_construccion = models.PositiveSmallIntegerField()
	dimensiones_terreno = models.CharField(max_length=30)
	dimensiones_edificio = models.CharField(max_length=30)
	TIPO_CONSTRUCCION_CHOICES = (
		(0, 'Iglesia'),
		(1, 'Capilla'),
		(2, 'Otro'),
	)
	tipo_construccion = models.SmallIntegerField()
	METODO_CONSTRUCCION_CHOICES = (
		(0, 'Nueva Edificacion'),
		(1, 'Otro'),
	)
	metodo_construccion = models.SmallIntegerField()
	requiere_permiso_construccion = models.BooleanField()
	is_icm_approved = models.BooleanField()
	moneda_local = models.CharField(max_length=20)
	dolar_en_moneda_local = models.DecimalField(max_digits=6, decimal_places=3)

	""" Informacion Financiera """
	# Contribuciones estimadas de la congregacion
	labor_moneda_local = models.DecimalField(max_digits=12, decimal_places=3)
	labor_dolares = models.DecimalField(max_digits=12, decimal_places=3)
	materiales_moneda_local = models.DecimalField(max_digits=15, decimal_places=3)
	materiales_dolares = models.DecimalField(max_digits=15, decimal_places=3)
	dinero_moneda_local = models.DecimalField(max_digits=15, decimal_places=3)
	dinero_dolares = models.DecimalField(max_digits=15, decimal_places=3)
	terreno_moneda_local = models.DecimalField(max_digits=12, decimal_places=3)
	terreno_dolares = models.DecimalField(max_digits=12, decimal_places=3)

	""" Otras fuentes de fondos """
	fuente1 = models.CharField(max_length=30)
	aporte_fuente1_monedalocal = models.DecimalField(max_digits=12, decimal_places=3)
	aporte_fuente1_dolares = models.DecimalField(max_digits=12, decimal_places=3)
	fuente2 = models.CharField(max_length=30)
	aporte_fuente2_monedalocal = models.DecimalField(max_digits=12, decimal_places=3)
	aporte_fuente2_dolares = models.DecimalField(max_digits=12, decimal_places=3)
	aporte_solicitado_monedalocal = models.DecimalField(max_digits=12, decimal_places=3)
	aporte_solicitado_dolares = models.DecimalField(max_digits=12, decimal_places=3)
	coste_total_monedalocal = models.DecimalField(max_digits=12, decimal_places=3)
	coste_total_dolares = models.DecimalField(max_digits=12, decimal_places=3)