from django.shortcuts import render, redirect
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.contrib.auth.decorators import login_required
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
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
                I have more things I want to do with it".
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
    update views,its named as <nam_of_app>/<name_of_model>_form.html.
    i.e insta/post_form.html
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


# Class-based view to update post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    ''' Yo have to use UserPassesTestMixin so that to check if the 
        user who create the post (instagrammer in our case) is the 
        one who update it because we want people who wrote the post
        is the one responsible to edit it.
    '''
    model = Post
    fields = ['posts', 'caption']

    def form_valid(self, form):
        form.instance.instagrammer = self.request.user
        return super().form_valid(form)

    ''' The method below is the one which the UserPassesTestMixin will
        run in order to see if the user passes a certain test condtion.
    '''

    def test_func(self):
        ''' get_object() function will helps to get get the exact post
            user is currently trying to update.
        '''
        post = self.get_object()
        ''' To get the currently logged in user is the one who created
            the post, use the below condition:-
        '''
        if self.request.user == post.instagrammer:
            return True
        return False


# Class-based view to delete post
''' By convention the template made used by which will be used by delete view, 
    its named in form of <name_of_app>/<name_of_model>_confirm_delete.html.
    i.e insta/post_confirm_delete.html

'''


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # to redirect to the preferred route
    # success_url = '/'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.instagrammer:
            return True
        return False


@login_required
def search(request):
    return render(request, 'insta/search.html')


@login_required
def notification(request):
    return render(request, 'insta/notification.html')


@login_required
def message(request):
    return render(request, 'insta/message.html')
