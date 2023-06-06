from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import *
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from JLPT.models import *
# from .models import Document

# Create your views here.
def list(request):
   profile = Profile.objects.get(user = request.user)
   Data = {
       'Posts': Post.objects.all().order_by('-date'),
       'profile' : profile
    }
   return render(request, 'Document/document.html', Data)

def document_list(request,number):
    search = request.GET.get('search')
    if search == '' or search is None:
        search = ''
        post = Post.objects.all().filter(user=request.user)
    else:
        post = Post.objects.filter(name__icontains = search)
    paginator = Paginator(post,10)
    page_obj = paginator.page(number)
    context = {
        'page_obj' : page_obj,
        'search' :search,
        'number' : number
    }
    return render(request,'Document/document_list.html',context)

def edit_document(request,pk):
    document = get_object_or_404(Post,id = pk)
    if request.method == "POST":
        print("POST")
        form = AddDocumentForm(request.POST, request.FILES,instance = document)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('Teacher:DetailDocument',pk=form.instance.id)
        else:
            print("Form is not valid")
            print(form.cleaned_data)
    form = AddDocumentForm(instance=document)
    return render(request,'Document/edit_document_form.html',{'form' : form})
def document_detail(request,pk):
    post = get_object_or_404(Post,id = pk)
    profile = Profile.objects.get(user = request.user)
    return render(request, 'Document/document_detail_main.html',{'post': post,'profile' : profile})