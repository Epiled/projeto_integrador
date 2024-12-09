from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Produto

class ProdutoListView(ListView):
  model = Produto
  template_name = 'product-list.html'

class ProdutoDetailView(DetailView):
  model = Produto
  template_name = 'product-details.html'

class ProdutoCreateView(CreateView):
  model = Produto
  template_name = 'product-form.html'
  fields = ['nome', 'descricao', 'valor']
  success_url = reverse_lazy('product-list')

class ProdutoDeleteView(DeleteView):
  model = Produto
  template_name = 'product-confirm-delete.html'
  success_url = reverse_lazy('product-list')

class ProdutoUpdateView(UpdateView):
  model = Produto
  template_name = 'product-form.html'
  fields = ['nome', 'descricao', 'valor']
  success_url = reverse_lazy('product-list')
