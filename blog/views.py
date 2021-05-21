from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Blog


# Create your views here.
class BlogLogin(LoginView):
    template_name = 'blog/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('blogs')

class RegisterView(FormView):
    template_name = 'blog/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('blogs')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterView,self).form_valid(form)

    def get(self,*agrs,**kwargs):
        if self.request.user.is_authenticated:
            redirect('blogs')
        return super(RegisterView,self).get(*agrs,**kwargs)

class BlogList(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = context['blogs'].filter(user=self.request.user)
        return context

class BlogDetail(LoginRequiredMixin,DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog.html'

class BlogCreate(LoginRequiredMixin,CreateView):
    model = Blog
    fields = ['title','author','content']
    success_url = reverse_lazy('blogs')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogCreate,self).form_valid(form)

class BlogUpdate(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ['title','author','content']
    success_url = reverse_lazy('blogs')

class BlogDelete(LoginRequiredMixin,DeleteView):
    model = Blog
    context_object_name = 'blog'
    success_url = reverse_lazy('blogs')

