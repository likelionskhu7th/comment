from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Article
from .forms import ArticleForm


# Create your views here.
def board(request):
    articles = Article.objects.all()
    return render(request, "blog/board.html", {"articles": articles})


def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "blog/detail.html", {"article": article})


def post_form(request, article_id=None):
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article_id)
        if form.is_valid():
            article = form.save(commit=False)
            article.title = form.cleaned_data["title"]
            article.content = form.cleaned_data["content"]
            article.published_at = timezone.now()
            article.save()
            return redirect("blog:detail", article.id)
    else:
        form = ArticleForm(instance=article_id)
        return render(request, "blog/post.html", {'form': form})


def post_new(request):
    return post_form(request)


def post_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return post_form(request, article)


def post_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect("blog:board")
