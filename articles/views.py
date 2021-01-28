import json
import logging
import random

from django.shortcuts import render
from django.views import View
from app_utils.utils import get_content_detail, get_quotes_list, get_randomized_quotes
from comments.models import Comment

logger = logging.getLogger(__name__)


class ArticleDetailView(View):
    template_name = 'articles/detail.html'

    def get(self, request, article_uuid):
        article = get_content_detail(str(article_uuid))
        quotes = get_randomized_quotes(get_quotes_list())
        comments = Comment.objects.filter(uuid=article_uuid)
        return render(request, self.template_name, {'article': article,
                                                    'quotes': quotes,
                                                    'comments':comments})
