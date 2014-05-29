# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Congregacion.foto_pastor'
        db.add_column(u'db_congregacion', 'foto_pastor',
                      self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'Edificacion.foto_construccion'
        db.add_column(u'db_edificacion', 'foto_construccion',
                      self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Congregacion.foto_pastor'
        db.delete_column(u'db_congregacion', 'foto_pastor')

        # Deleting field 'Edificacion.foto_construccion'
        db.delete_column(u'db_edificacion', 'foto_construccion')


    models = {
        u'db.adjuntos': {
            'Meta': {'object_name': 'Adjuntos'},
            'archivo_adjunto': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_archivo': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'db.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'ciudad_cercana': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'distancia_ciudad': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'distancia_iglesia': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'edificacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db.Edificacion']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iglesia_cercana': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'poblacion_comunidad': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'db.condiciones': {
            'Meta': {'object_name': 'Condiciones'},
            'aceptacion': ('django.db.models.fields.BooleanField', [], {}),
            'actividades': ('django.db.models.fields.BooleanField', [], {}),
            'alcance': ('django.db.models.fields.BooleanField', [], {}),
            'comentarios': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'construccion': ('django.db.models.fields.BooleanField', [], {}),
            'discipulado': ('django.db.models.fields.BooleanField', [], {}),
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            'found_commitment': ('django.db.models.fields.BooleanField', [], {}),
            'found_payment': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'found_trust': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mantenimiento': ('django.db.models.fields.BooleanField', [], {}),
            'nombre_completo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'presupuesto': ('django.db.models.fields.BooleanField', [], {}),
            'terminacion': ('django.db.models.fields.BooleanField', [], {})
        },
        u'db.congregacion': {
            'Meta': {'object_name': 'Congregacion'},
            'anios_iglesia': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'anios_ministerio': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'asistentes_adultos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'asistentes_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'edificacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db.Edificacion']", 'unique': 'True'}),
            'entrenamiento_biblico': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'estado_civil': ('django.db.models.fields.SmallIntegerField', [], {}),
            'fecha_fundacion': ('django.db.models.fields.DateField', [], {}),
            'foto_pastor': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'hay_material': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingresos_ofrendas': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'lengua_primaria': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'miembros_adultos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'miembros_ninos': ('django.db.models.fields.SmallIntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre_pastor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numero_hijos': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'q1_why_not': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'q2_how_do': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'q2_why_not': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titulos_obtenidos': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'usa_material': ('django.db.models.fields.BooleanField', [], {})
        },
        u'db.edificacion': {
            'Meta': {'object_name': 'Edificacion'},
            'coordenadas': ('djgeojson.fields.PointField', [], {}),
            'dimensiones_edificio': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dimensiones_terreno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.SmallIntegerField', [], {}),
            'foto_construccion': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_icm_approved': ('django.db.models.fields.BooleanField', [], {}),
            'metodo_construccion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'moneda_local': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nombre_proyecto': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'owner_escritura': ('django.db.models.fields.SmallIntegerField', [], {}),
            'requiere_permiso': ('django.db.models.fields.BooleanField', [], {}),
            'tiempo_limite': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'tipo_adquisicion': ('django.db.models.fields.SmallIntegerField', [], {}),
            'tipo_construccion': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'db.fuentes_financieras': {
            'Meta': {'object_name': 'Fuentes_Financieras'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'edificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['db.Edificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'})
        },
        u'db.informacionfinanciera': {
            'Meta': {'object_name': 'InformacionFinanciera'},
            'aporte_terreno': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'costo_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'dinero_efectivo': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'edificacion': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['db.Edificacion']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mano_obra': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'}),
            'pago_fondo': ('django.db.models.fields.SmallIntegerField', [], {}),
            'valor_materiales': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'valor_solicitado': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '3'})
        }
    }

    complete_apps = ['db']