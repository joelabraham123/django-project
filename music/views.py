from django.views import generic
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album
#these two are for user registration..login provides a session id
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album #what type of object you r taking detail
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    #mention which fields u want user to fill out
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index') #since u r deleting,it will not make a new form..it will redirect u to home page

class UserFormView(View):
    form_class = UserForm       #this is a blueprint which u have to provide every time u make such classes
    template_name = 'music/registration_form.html'

#this shortcut logic is for pages where both methods are possible to be used
    def get(self,request):  #displays a blank form for adding a new entry
        form = self.form_class(None)    #none because by default it has no data..user has to fill it
        return render(request,self.template_name, {'form':form})

    def post(self,request):     #adds entry user submitted to database
        form = self.form_class(request.POST)

        if form.is_valid(): #django automatically validates and tells if form is valid and details given by user are proper
            user = form.save(commit=False)  #this line stores info locally for normalizing(cleaning) before storing in database

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password) #to generate another hashed password for the entered password
            user.save() #this line finally saves to database the new user

            user = authenticate(username = username, password = password) #this checks with database if they are actual user

            if user is not None:    #if credentials are matched
                if user.is_active:      #see if the user was banned previously but data is still present
                    login(request,user)     #logs user into our website
                    return redirect('music:index')

        return render(request,self.template_name, {'form':form})



