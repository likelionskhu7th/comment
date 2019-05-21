from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def board(request):
    articles = Article.objects.all()
    return render(request, "blog/board.html", {"articles": articles})


def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect("blog:detail", article_id)
    else:
        form = CommentForm()
        return render(request, "blog/detail.html", {"article": article, "form": form})


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


def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect("blog:detail", comment.article.id)


def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    article = comment.article
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect("blog:detail", article.id)
    else:
        form = CommentForm(instance=comment)
        return render(request, "blog/post.html", {"form": form})


def post_new(request):
    return post_form(request)


def post_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return post_form(request, article)


def post_delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect("blog:board")
