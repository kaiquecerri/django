from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    # Pagina principal do Projeto
    return render(request, 'projetos_iniciais/index.html')

@login_required
def topics(request):
    # Pagina de topicos
    topic = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topic}

    return render(request, 'projetos_iniciais/topics.html', context)

@login_required
def topic(request, topic_id):
    #Pagina de um topico especifico
    topic = Topic.objects.get(id = topic_id)
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'projetos_iniciais/topic.html', context)
    
        

@login_required
def new_topic(request):
    # Adiciona um novo topico
    if request.method != 'POST':
        # Nenhum dado recebido: criar formulario novo
        form = TopicForm()
    else:
        # Dados de POST recebidos: processar os recebidos
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'projetos_iniciais/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    #Criação de entrada em um tópico
    topic = Topic.objects.get(id = topic_id)
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Nenhum dado recebido: criar formulario novo
        form = EntryForm()
    else:   
        # Dados de POST recebidos: processar os recebidos
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic':topic, 'form': form}
    return render(request, 'projetos_iniciais/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    #Edição de uma entrada existente
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
            raise Http404
    
    if request.method != 'POST':
        # Não alterou: recebe os dados do entry
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))

    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'projetos_iniciais/edit_entry.html', context)
    

