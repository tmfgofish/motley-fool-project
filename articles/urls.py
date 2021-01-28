from django.urls import path
from .views import ArticleDetailView

"""
A more ideal implementation would utilize 
slugs in the article url pattern
"""

urlpatterns = [
    # path('<slug:article_slug>/<uuid:article_uuid>', ArticleDetailView.as_view(), name="article-detail"),
    path('<uuid:article_uuid>', ArticleDetailView.as_view(), name="article-detail"),
]