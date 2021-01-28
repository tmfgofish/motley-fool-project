from django.urls import path
from .views import CommentView


urlpatterns = [
    path('<uuid:article_uuid>', CommentView.as_view(), name='comment-view'),
]