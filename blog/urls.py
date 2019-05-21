from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.board, name="board"),
    path("board/<int:article_id>/", views.detail, name="detail"),
    path("new/", views.post_new, name="post_new"),
    path("edit/<int:article_id>/", views.post_edit, name="post_edit"),
    path("delete/<int:article_id>/", views.post_delete, name="post_delete"),
    path("comment_edit/<int:comment_id>/", views.comment_edit, name="comment_edit"),
    path("comment_delete/<int:comment_id>/", views.comment_delete, name="comment_delete"),
]
