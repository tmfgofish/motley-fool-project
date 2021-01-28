import json
import logging
import random

from django.shortcuts import render
from django.views import View
from app_utils.utils import get_content_list, get_randomized_content

logger = logging.getLogger(__name__)


class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        headline_content = []
        content = get_content_list()
        for article in content['results']:
            for tag in article['tags']:
                if tag['slug'] == '10-promise':
                    headline_content.append(article)
        randomized_content = get_randomized_content(content, headline_content[0]['uuid'])
        return render(request, self.template_name, {'headline_article': headline_content[0],
                                                    'randomized_content': randomized_content})
