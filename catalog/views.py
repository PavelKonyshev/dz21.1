from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from .models import Category, Product

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

class ContactPageView(TemplateView):
    template_name = "catalog/contacts.html"

