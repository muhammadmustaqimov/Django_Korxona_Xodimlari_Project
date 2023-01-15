from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class XodimListView(ListView):
    def get(self, request, **kwargs):
        search = self.request.GET.get('search')
        print(search)
        customers = Post.objects.all()
        if (search):
            customers = Post.objects.filter(fullname__contains=search)

        return render(request, 'home.html', {'customers': customers})

    model = Post
    template_name = 'home.html'


class XodimDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class XodimCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['img', 'fullname', 'author', 'position', 'about']


class XodimUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['img', 'fullname', 'author', 'position', 'about']


class XodimDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


def main(request):

    if request.method == 'GET':

        # getting all the objects of hotel.
        all = Post.objects.all()
        return render(request, "test.html", {'all': all})
