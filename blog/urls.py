from django.urls import path
from .views import BlogCreateView,BlogDeleteView,BlogListView,BlogRetrieveView,BlogUpdateView,CommentCreateView,CommentListView,CommentDeleteView,CommentRetrieveView,CommentUpdateView,BlogLikeView

urlpatterns = [
    path("", BlogListView.as_view()),
    path("create/", BlogCreateView.as_view()),
    path("<int:pk>/", BlogRetrieveView.as_view()),
    path("<int:pk>/update/", BlogUpdateView.as_view()),
    path("<int:pk>/delete/", BlogDeleteView.as_view()),
    path("<int:pk>/like/", BlogLikeView.as_view()),

    path("comments/", CommentListView.as_view()),
    path("comments/create/", CommentCreateView.as_view()),
    path("comments/<int:pk>/", CommentRetrieveView.as_view()),
    path("comments/<int:pk>/update/", CommentUpdateView.as_view()),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view()),
]