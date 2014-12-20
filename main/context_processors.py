from db.models import Etapa, Edificacion
from usuarios.models import Usuario

def notificaciones(request):
	etapas = {}
	if request.user.is_authenticated():
		if request.user.tipo == Usuario.NACIONAL:
			etapas = Etapa.objects.filter().order_by('-created', '-pk')[:20]
		elif request.user.tipo == Usuario.REGIONAL:
			pass
		elif request.user.tipo == Usuario.LOCAL:
			edificaciones_user = Edificacion.objects.filter(usuario=request.user)
			etapas = []
			for e in edificaciones_user:
				etapas += e.etapa_set.all()[:20]
			etapas = sorted(etapas, key=lambda etapa: -etapa.pk)
	return {'etapas': etapas}