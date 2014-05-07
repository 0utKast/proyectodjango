from django.conf.urls import patterns,include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^preguntas/$', 'preguntasyrespuestas.views.index', name='preguntas'),
    url(r'^preguntas/(?P<pregunta_id>\d+)/$', 'preguntasyrespuestas.views.pregunta_detalle', name='pregunta_detalle'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^preguntas/crear/$','preguntasyrespuestas.views.pregunta_crear', name="pregunta_crear"),
    url(r'^preguntas/editar/(?P<pregunta_id>\d+)/$','preguntasyrespuestas.views.pregunta_editar', name='pregunta_editar'),
    url(r'^login/$', 'miprimerproyecto.views.login_page', name="login"),

)
   











