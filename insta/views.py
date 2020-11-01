from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import(
    ListView,
    DetailView,
    CreateView
)
from .forms import PostForm
from .models import Post

# Create your views here.


@login_required
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'insta/home.html', context)

# Class-based view to list/retrieve post


class PostListView(ListView):

    ''' Create a variable called model which tells the ListView
        what model to query in order to create the list.
    '''
    model = Post

    ''' By default class-based view looks for template in 
        form of <app>/<model>_<viewtype>.html i.e 
        insta/post_list.html (in our case), but we can 
        change that by defining new template using template name.
    '''
    template_name = 'insta/home.html'

    ''' By default our list view call the variable *object list*
        (the one in the template that is looping over eg.*posts* 
        as defined in function-based view). So we can change the
        *posts* in our template so that is looping over *object list* 
        or we can set one more variable in our list view and let 
        our class-based view know we want that variable to be named
        as *posts* instead. 
    '''
    context_object_name = 'posts'

    ''' To change the order of posts listed i.e from newest to oldest,
        change the order our query is making to the database. Therefore 
        add the ordering attribute with the field we want to order on.
        NB: -ve sign (from newest to oldest),+ve sign (form oldest to newest)
    '''

    ordering = ['-posts']


@login_required
def post_list(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'insta/post_list.html', context)


# Class-based view to detail a single post
class PostDetailView(DetailView):
    ''' If we stick to the convention (create a template with 
        the naming convention that our view will be looking i.e 
        in form of <app>/<model>_<viewtype>.html and use the variable
        name of *object list* inside the template in stead of *posts*), 
        only one line is needed i.e the one below 
    '''
    model = Post


@login_required
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            '''commit=False tells Django that
                "Don't send this to database yet, 
                I have more things I want to do with it.
            '''
            obj = form.save(commit=False)
            obj.instagrammer = request.user
            obj.save()
            # return redirect('insta-post_list')
            return redirect('insta-home')
    else:
        form = PostForm()

    context = {
        'form': form
    }

    return render(request, 'insta/upload_post.html', context)


# Class-based view to create post

''' By convention the template made will be used by create and 
    update views, its named in form of <name_of_model>_form.html.
    i.e post_form.html
'''

''' We shouldnt be able to create a post unless we are logged in
    as specific user i.e. if you want to create a post and you're 
    not logged in, you ll be redirected to login page. Therefore 
    LoginRequiredMixin is used instead of @login_requred decorator
    (because decorators are not used in class).
'''


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    ''' Set the field/s from the model created, you want to
        appear in the form. NB:order matter.
    '''
    fields = ['posts', 'caption']

    ''' Every post needs to have user who created it (instagrammer in our case),
        and the user associated with the post must be the current logged in user.
        In order to set it, is to override the form_valid method for our create
        view that will allow to add user before the form is submitted.
    '''

    def form_valid(self, form):
        form.instance.instagrammer = self.request.user
        return super().form_valid(form)


@login_required
def search(request):
    return render(request, 'insta/search.html')


@login_required
def notification(request):
    return render(request, 'insta/notification.html')


@login_required
def message(request):
    return render(request, 'insta/message.html')
