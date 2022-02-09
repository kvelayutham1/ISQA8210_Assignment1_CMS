from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Client, Comment, Vehicle
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.views import generic
from .forms import forms, CommentForm


class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client
    template_name = 'client_list.html'

    def get_queryset(self):
        return Client.objects.filter(author=self.request.user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    #    form_class = CommentForm
    template_name = 'add_comment.html'
    #    fields = ('comment', 'author', )
    fields = ('client', 'comment',)
    login_url = 'login'

    def form_valid(self, form):
        # In an effort to pass client.pk as initial value for client field
        #        client_id = self.request.POST.get('client_id')
        #        client_id = Client.objects.get(pk=self.kwargs['client.pk'])
        form.instance.author = self.request.user
        #        self.object = form.save(commit=False)
        #        self.object.client_ids = client_id
        #        form.instance.client_id = client_id
        #        self.object.save()
        return super().form_valid(form)


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'

    def get_queryset(self):
        return Vehicle.objects.filter(author=self.request.user)


#    def get_queryset(self):
#        return Vehicle.objects.filter(client=self.a)


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    fields = ('client', 'make', 'model', 'VIN_number', 'Date_of_Purchase', 'Date_of_LastService',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    login_url = 'login'


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = ('client', 'make', 'model', 'VIN_number', 'Date_of_Purchase', 'Date_of_LastService',)
    template_name = 'vehicle_edit.html'


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    success_url = reverse_lazy('client_list')
