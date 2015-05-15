# -*- coding: utf-8 -*-
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from datetime import date

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Submit, HTML, Button, Row, Field, Hidden
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, StrictButton, FieldWithButtons, UneditableField, InlineRadios, InlineCheckboxes, PrependedAppendedText

from db.models import Edificacion, Comunidad, Congregacion, Adjuntos, Condiciones, InformacionFinanciera, Comentario
from .datos import EDIFICACION_COORDENADAS

from map_field import widgets as map_widgets
from map_field import fields as map_fields
from usuarios.models import Usuario
from django.core.exceptions import ValidationError 


class ModelFormBase(forms.ModelForm):
            
    def quien_soy(self):
        return self.instance

class EdificacionForm(ModelFormBase):  

    class Meta:
        model = Edificacion
        exclude = ['estado', 'usuario', 'etapa_actual', 'ingeniero', 'arquitecto', 'tesorero',
                    'aprobacion_regional', 'aprobacion_arquitecto', 
                    'aprobacion_ingeniero', 'aprobacion_nacional', 'aprobacion_tesorero', 'created', 'updated', 
                    'requiere_arquitecto','aprobacion_internacional', 'usuarios_asignados', 'planos_creados']

    def __init__(self, *args, **kwargs):
        super(EdificacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.form_class       = 'form-horizontal'
        self.helper.form_tag         = False
        self.helper.label_class      = 'col-sm-3'
        self.helper.field_class      = 'col-sm-9'
        self.fields['coordenadas'].widget = map_widgets.MapsGeoPointhWidget()

        # Esta es una manera mas sencilla de agregar atributos a los campos
        self.helper.all().wrap(Field, css_class='input-sm') 
        self.helper['direccion'].wrap(Field, css_class="input-xlarge", rows="2")
        self.helper['coordenadas'].wrap(Field, css_class="geolocation_field")
        self.helper.filter_by_widget(forms.Select).wrap(InlineRadios) 


class InformacionFinancieraForm(ModelFormBase):
    
    class Meta:
        model = InformacionFinanciera
        exclude = ['edificacion']
                    

    def __init__(self, *args, **kwargs):
        super(InformacionFinancieraForm, self).__init__(*args, **kwargs)        
        self.helper = FormHelper(self)

        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

        self.helper.all().wrap(Field, css_class='input-sm') 
        self.helper.filter_by_widget(forms.Select).wrap(InlineRadios)

class ComunidadForm(ModelFormBase):
    
    class Meta:
        model = Comunidad
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(ComunidadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

        self.helper.all().wrap(Field, css_class='input-sm')


class CongregacionForm(ModelFormBase):
    
    class Meta:
        model = Congregacion
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(CongregacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.fields['fecha_fundacion'].widget = SelectDateWidget(years=( range(1900, date.today().year + 1) ) )
       
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'

        self.fields['titulos_obtenidos'].widget = forms.TextInput(attrs={'placeholder': 'Tecnico en Biblia, Master en Biblia'})
      
        self.helper.all().wrap(Field, css_class='input-sm')
        self.helper.filter_by_widget(forms.Textarea).wrap(Field, css_class="input-xlarge", rows="2") 
        self.helper.filter_by_widget(SelectDateWidget).wrap(Field, css_class="input-sm", style="width:110px; float:left; margin-right:5px;") 
        self.helper.filter_by_widget(forms.Select).wrap(InlineRadios)
        #self.fields['titulos_obtenidos'].widget = FilteredSelectMultiple("verbose name", is_stacked=False)

class CondicionesForm(ModelFormBase):
    
    class Meta:
        model = Condiciones
        exclude = ['edificacion']

    def __init__(self, *args, **kwargs):
        super(CondicionesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_tag = False
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-8'

        self.helper.all().wrap(Field, css_class='input-sm')
        self.helper.filter_by_widget(forms.Select).wrap(InlineRadios)
        self.helper.filter_by_widget(forms.Textarea).wrap(Field, css_class="input-xlarge", rows="4") 

class AdjuntosForm(ModelFormBase):
    
    class Meta:
        model = Adjuntos
        exclude = ['edificacion', 'planos_arquitecto']

    def __init__(self, *args, **kwargs):
        super(AdjuntosForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_tag     = False
        self.helper.label_class  = 'col-sm-3'
        self.helper.field_class  = 'col-sm-9'


#class FuentesFinanciacionForm(forms.ModelForm):
    
#    class Meta:
#        model = FuentesFinanciacion
#        exclude = ['info_financiera']

#    def __init__(self, *args, **kwargs):
#        super(FuentesFinanciacionForm, self).__init__(*args, **kwargs)
#        self.helper = FormHelper(self)
        
#        self.helper.form_tag = False
#        self.helper.label_class = 'col-sm-3'
#        self.helper.field_class = 'col-sm-9'

    
class ComentarioForm(forms.ModelForm):
    """Formulario para crear un comentario"""
    
    class Meta:
        model = Comentario
        exclude = ['edificacion', 'commenter', 'created']

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_show_labels = False
        self.helper.form_id = 'comentario-form'
        self.helper.form_class = 'clearfix'


        self.helper.layout = Layout(
            PrependedText('descripcion', "<i class='fa fa-user '></i>", placeholder="Agrega tu comentario", rows="1", ng_focus="procesarFoco($event)", ng_blur="procesarFoco($event)"),
            Field('comentario_padre', type="hidden"),
            FormActions(
                StrictButton('Enviar', type="Submit", css_class="btn-info pull-right btn-xs", ng_show="verSubmit", ng_click="alClickComentario($event)", data_loading_text="Enviando...", autocomplete="off"),
            )
        )


""" FORMULARIOS AUTORIZACION """

class AprobacionForm(forms.Form):  
    aprobar = forms.CharField(initial='True')

    def __init__(self, *args, **kwargs):
        super(AprobacionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag  = False
        self.helper.form_show_labels =False

        self.helper.layout = Layout(
            Field('aprobar', type='hidden'),
            FormActions(
                StrictButton('Revisar de nuevo', id="revisar-aprobacion-btn", type="button", css_class="btn btn-default", data_dismiss="modal"),
                StrictButton('Estoy seguro', id="submit-aprobacion-btn", type="Submit", css_class="btn btn-primary", 
                    data_loading_text="<i class='fa fa-spinner fa-spin'></i> Procesando...", ng_click="alClickAprobacion()"),
            )
        )


class AprobacionInternacionalForm(ModelFormBase):  
    class Meta:
        model = Edificacion
        fields = ['aprobacion_internacional']         

def validate_planos(value):
    print('Aqui estoy')
    if value != None:       
        raise ValidationError(u'Debe subir planos para poder aprobar')

class PlanosArquitectoForm(ModelFormBase):
    """Aqui se subiran los planos del arquitecto antes de que de su autorizacion"""
    planos_arquitecto = forms.FileField('Planos', validators=[validate_planos])

    class Meta:
        model = Adjuntos
        fields = ['planos_arquitecto']


class AprobacionArquitectoForm(ModelFormBase):
    class Meta:
        model = Edificacion
        fields = ['aprobacion_arquitecto']

    # def save(self, planos, commit=True):
    #     print('Datos', self.fields['planos'])
    #     instance = super(AprobacionArquitectoForm, self).save(commit=False)
    #     adj = Adjuntos.objects.get(edificacion=instance)
    #     adj.planos_arquitecto = planos
    #     adj.save()
    #     if commit:
    #         instance.save()
    #     return instance
  
class AprobacionIngenieroForm(ModelFormBase):  
    class Meta:
        model = Edificacion
        fields = ['aprobacion_ingeniero']

class AprobacionTesoreroForm(ModelFormBase):  
    class Meta:
        model = Edificacion
        fields = ['aprobacion_tesorero']

class AprobacionNacionalForm(ModelFormBase):  
    class Meta:
        model = Edificacion
        fields = ['aprobacion_nacional']


""" FORMULARIOS ASIGNACION Y EDICCION DE USUARIOS """

class AsignarUsuariosForm(ModelFormBase):

    def __init__(self, *args, **kwargs):
        super(AsignarUsuariosForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_action = "home"

        self.fields['arquitecto'].queryset = Usuario.objects.filter(tipo=Usuario.ARQUITECTO)
        self.fields['ingeniero'].queryset = Usuario.objects.filter(tipo=Usuario.INGENIERO)
        self.fields['tesorero'].queryset = Usuario.objects.filter(tipo=Usuario.TESORERO)

        self.helper.layout = Layout(
            PrependedAppendedText('arquitecto', "<i class='fa fa-user fa-fw'></i>", "arquitecto <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            PrependedAppendedText('ingeniero', "<i class='fa fa-user fa-fw'></i>", "dir. obra <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            PrependedAppendedText('tesorero', "<i class='fa fa-user fa-fw'></i>", "tesorero <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            StrictButton('Guardar usuarios', type="Submit", css_class="btn-info btn-sm"),
        )

    class Meta:
        model  = Edificacion
        fields = ['arquitecto', 'ingeniero', 'tesorero']


class ArquitectoEditForm(ModelFormBase):

    def __init__(self, *args, **kwargs):
        super(ArquitectoEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_action = "home"  # es reemplazado en la vista

        self.fields['arquitecto'].queryset = Usuario.objects.filter(tipo=Usuario.ARQUITECTO)
        self.fields['arquitecto'].empty_label = None

        self.helper.layout = Layout(
            Hidden('editar', Usuario.ARQUITECTO),
            PrependedAppendedText('arquitecto', "<i class='fa fa-user fa-fw'></i>", "arquitecto <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            StrictButton('Cambiar arquitecto', type="Submit", css_class="btn-info btn-sm"),
        )

    class Meta:
        model  = Edificacion
        fields = ['arquitecto']

class IngenieroEditForm(ModelFormBase):

    def __init__(self, *args, **kwargs):
        super(IngenieroEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_action = "home"  # es reemplazado en la vista

        self.fields['ingeniero'].queryset = Usuario.objects.filter(tipo=Usuario.INGENIERO)
        self.fields['ingeniero'].empty_label = None

        self.helper.layout = Layout(
            Hidden('editar', Usuario.INGENIERO),
            PrependedAppendedText('ingeniero', "<i class='fa fa-user fa-fw'></i>", "dir. obra <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            StrictButton('Cambiar dir. de obra', type="Submit", css_class="btn-info btn-sm"),
        )

    class Meta:
        model  = Edificacion
        fields = ['ingeniero']


class TesoreroEditForm(ModelFormBase):

    def __init__(self, *args, **kwargs):
        super(TesoreroEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.form_action = "home"  # es reemplazado en la vista

        self.fields['tesorero'].queryset = Usuario.objects.filter(tipo=Usuario.TESORERO)
        self.fields['tesorero'].empty_label = None

        self.helper.layout = Layout(
            Hidden('editar', Usuario.TESORERO),
            PrependedAppendedText('tesorero', "<i class='fa fa-user fa-fw'></i>", "tesorero <a href='/admin/usuarios/usuario/add/'><i class='fa fa-plus'></i></a>", css_class="input-sm"),
            StrictButton('Cambiar tesorero', type="Submit", css_class="btn-info btn-sm"),
        )

    class Meta:
        model  = Edificacion
        fields = ['tesorero']