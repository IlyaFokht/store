from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView  # импортируем класс получения деталей объекта
from .models import Post
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm

class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering=['-dateCreation']
    paginate_by = 3

    def get_filter(self):
        return PostFilter(self.request.GET,queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs



    def get_context_data(self,*args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            "filter": self.get_filter()
        }


class PostUpdate(UpdateView):
    template_name = 'add.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)



class PostAdd(CreateView):
    template_name = 'add.html'
    form_class = PostForm
    success_url = '/news/'

class PostDelete(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

# создаём представление, в котором будут детали конкретного отдельного товара
class PostsDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объекта. в нём будет




class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['-dateCreation']
    paginate_by = 5

    def get_filter(self):
        return PostFilter(self.request.GET,queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self,*args, **kwargs):
        return {
                **super().get_context_data(*args,**kwargs),
                "filter":self.get_filter()

        }