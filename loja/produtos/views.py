from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Especiaria, Artefato, Quadro, Livro
from django.urls import reverse_lazy
# Create your views here.

class EspeciariaCreate(CreateView):
    model = Especiaria
    fields = ['nome','valor','disponibilidade','descricao']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-especiaria')


class ArtefatoCreate(CreateView):
    model = Artefato
    fields = ['nome','valor','disponibilidade','descricao','tipo']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-artefato')


class QuadroCreate(CreateView):
    model = Quadro
    fields = ['nome','valor','disponibilidade','descricao','autor']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-quadro')


class LivroCreate(CreateView):
    model = Livro
    fields = ['nome','valor','disponibilidade','descricao','isbn']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-livro')

class EspeciariaUpdate(UpdateView):
    model = Especiaria
    fields = ['nome','valor','disponibilidade','descricao']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-especiaria')

class ArtefatoUpdate(UpdateView):
    model = Artefato
    fields = ['nome', 'valor', 'disponibilidade', 'descricao', 'tipo']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-artefato')

class QuadroUpdate(UpdateView):
    model = Quadro    
    fields = ['nome','valor','disponibilidade','descricao','autor']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-quadro')

class LivroUpdate(UpdateView):
    model = Livro
    fields = ['nome','valor','disponibilidade','descricao','isbn']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('listar-livro')

class EspeciariaDelete(DeleteView):
    model = Especiaria
    template_name = 'produtos/excluir.html'
    success_url = reverse_lazy('listar-especiaria')

class ArtefatoDelete(DeleteView):
    model = Artefato
    template_name = 'produtos/excluir.html'
    success_url = reverse_lazy('listar-artefato')

class QuadroDelete(DeleteView):
    model = Quadro
    template_name = 'produtos/excluir.html'
    success_url = reverse_lazy('listar-quadro')

class LivroDelete(DeleteView):
    model = Livro
    template_name = 'produtos/excluir.html'
    success_url = reverse_lazy('listar-livro')

class EspeciariaList(ListView):
    model = Especiaria
    template_name = 'produtos/lista/especiaria.html'

class ArtefatoList(ListView):
    model = Artefato
    template_name = 'produtos/lista/artefato.html'

class QuadroList(ListView):
    model = Quadro
    template_name = 'produtos/lista/quadro.html'

class LivroList(ListView):
    model = Livro
    template_name = 'produtos/lista/livro.html'
