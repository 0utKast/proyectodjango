from django.http import HttpResponse,Http404
from preguntasyrespuestas.models import Pregunta
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from preguntasyrespuestas.form import PreguntaForm
from django.utils import timezone

def index(request):
    preguntas = Pregunta.objects.all()
    return render_to_response('preguntasyrespuestas/index.html',
                                      {'preguntas': preguntas})


def pregunta_detalle (request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    return render_to_response('preguntasyrespuestas/pregunta_detalle.html',
                                        {'pregunta': pregunta})

def pregunta_crear(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preguntas')
    else:
        form = PreguntaForm()
    return render_to_response('preguntasyrespuestas/pregunta_crear.html',
                   {'form': form},
                   context_instance=RequestContext(request))

def pregunta_editar(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
    if request.method == 'POST':
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
            return redirect('pregunta_detalle', pregunta_id)
    else:
        form = PreguntaForm(instance=pregunta)
    return render_to_response('preguntasyrespuestas/pregunta_editar.html',
                                             {'form': form},
                   context_instance=RequestContext(request))

#[template_directory]/preguntasyrespuestas/index.html
