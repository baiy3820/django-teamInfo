from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Teamer, Choice
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'teamInfo/index.html'
    context_object_name = 'latest_voice_list'

    def get_queryset(self):
        return Teamer.objects.order_by('-Birthday')[:5]

def index(request):
    latest_voice_list = Teamer.objects.order_by('-Birthday')[:5]
    template = loader.get_template('teamInfo/index.html')
    context = RequestContext(request, {
        'latest_voice_list': latest_voice_list,
    })
    return HttpResponse(template.render(context))

class DetailView(generic.DetailView):
    model = Teamer
    template_name = 'teamInfo/detail.html'

def detail(request, voice_id):
    voice = get_object_or_404(Teamer, pk=voice_id)
    return render(request, 'teamInfo/detail.html', {'voice': voice})

class ResultsView(generic.DetailView):
    model = Teamer
    template_name = 'teamInfo/results.html'

def results(request, voice_id):
    voice = get_object_or_404(Teamer, pk=voice_id)
    return render(request, 'teamInfo/results.html', {'voice': voice})

def vote(request, voice_id):
    v = get_object_or_404(Teamer, pk=voice_id)
    try:
        selected_choice = v.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'teamInfo/detail.html', {
            'voice': v,
            'error_message': "You didn't give your opinion about the Voice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('teamInfo:results', args=(v.id,)))
