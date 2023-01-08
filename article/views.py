from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, Http404, redirect, reverse
from .models import Article
import random
from .forms import ArticleForm

def _index(request):
    _id = random.randint(1, 4)
    obj = Article.objects.get(id=_id)

    title = obj.content
    content = obj.content
    HTML_CONTENT = f"""
    <h1>{title} (id: {obj.id})</h1>
    <p>{content}</p1>
"""
    return HttpResponse(HTML_CONTENT)




def index(request):
    articles = Article.objects.filter(is_deleted__exact=False).order_by('-id')
    q = request.GET.get('q')
    if q:
        articles = articles.filter(title__icontains=q)
    return render(request,'article/index.html',{'object_list': articles})


def detail(request,slug=None):
    context = {}
    if slug:
        article = Article.objects.get(slug=slug)
        context['object'] = article
        return render(request,'article/detail.html', context)
    return Http404


def _create(request):
    context = {
        "created": False
    }
    if request.method == "POST":
        title =  request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(titlle=title,content=content)
        context['object'] = article
        context['created'] = True
        # return redirect(reverse('articles:detail',kwargs={"pk": article.id}))
    return render(request,'article/create.html',context)




def create(request):
    form = ArticleForm(request.POST or None, files=request.FILES)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        messages.success(request, f"Muvaffaqiyatli yangi xabar qoshdingiz")

        if form.is_valid():
            form.save()
            return redirect('article:list')
    context = {
        'form': form
    }

    return render(request, 'article/create.html', context)


@login_required(login_url='/auth/login/')
def edit(request, slug):
        article = Article.objects.get(slug=slug)
        form = ArticleForm(instance=article)
        if request.method == 'POST':
            form = ArticleForm(data=request.POST, instance=article, files=request.FILES)
            form.save()
            messages.success(request, "Muvaffaqiyatli xabarni yangiladingiz ")
            return redirect(reverse('article:detail', kwargs={"slug": article.slug}))
        ctx = {
            'form': form

        }
        return render(request,'article/edit.html',ctx)

@login_required(login_url='/auth/login/')
def delete(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == "POST":
        article.is_deleted =True
        article.save()
        messages.error(request, f"Article ochirildi({article.id})")
        # article.delete()
        return redirect('article:list')
    context = {
        'object': article
    }
    return render(request, 'article/delete.html',context)



