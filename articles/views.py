from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from .forms import ArticleForm, CategoryForm
from .models import Article, Category


@login_required
def index_view(request):
    articles = Article.objects.all()
    categories = Category.objects.all()

    return render(request, 'articles/index.html', {
        'articles': articles,
        'categories': categories,
    })


@login_required
def create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()

            messages.success(request, _('Article has been created.'))
            return redirect('articles')
    else:
        form = ArticleForm()

    return render(request, 'articles/create.html', {
        'form': form,
    })


@login_required
def detail_view(request, pk):
    article = Article.objects.get(id=pk)

    return render(request, 'articles/detail.html', {
        'article': article,
    })


@login_required
def update_view(request, pk):
    article = Article.objects.get(id=pk)

    if request.user == article.user or request.user.is_superuser:
        pass
    else:
        messages.warning(request, _('You should not be here.'))
        return redirect('articles')

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()

            messages.success(request, _('Article has been updated.'))
            return redirect('articles')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'articles/update.html', {
        'form': form,
    })


@login_required
def delete_view(request, pk):
    article = Article.objects.get(id=pk)

    if request.user == article.user or request.user.is_superuser:
        pass
    else:
        messages.warning(request, _('You should not be here.'))
        return redirect('articles')

    if request.method == 'POST':
        article.delete()

        messages.success(request, _('Article has been deleted.'))
        return redirect('articles')

    return render(request, 'articles/delete.html', {
        'article': article,
    })


@login_required
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, _('Category has been created.'))
            return redirect('articles')
    else:
        form = CategoryForm()

    return render(request, 'articles/category_create.html', {
        'form': form,
    })


@login_required
def category_view(request, pk):
    category = Category.objects.get(id=pk)

    return render(request, 'articles/category.html', {
        'category': category,
    })
