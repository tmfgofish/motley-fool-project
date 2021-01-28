import json
import random

from django.utils.text import slugify


def get_content_list():
    data = open('JSON/content_api.json').read()
    json_data = json.loads(data)
    return json_data
    

def get_quotes_list():
    data = open('JSON/quotes_api.json').read()
    json_data = json.loads(data)
    return json_data


def get_content_detail(article_uuid):
    article_uuid = str(article_uuid)
    data = open('JSON/content_api.json').read()
    content = json.loads(data)
    for article in content['results']:
        if article['uuid'] == article_uuid:
            return article
    return False


def get_randomized_content(content, headline_uuid):
    """
    Fetches three random articles from the content API
    that excludes the headline article
    """
    randomized_content = []
    content = [article for article in content['results'] if article['uuid'] != headline_uuid]
    article_index = random.sample(range(1, len(content)), 3)
    for i in article_index:
        randomized_content.append(content[i])
    return randomized_content


def get_randomized_quotes(quotes):
    """
    Fetches three random quotes from the quotes API
    """
    randomized_quotes = []
    quotes_index = random.sample(range(1, len(quotes)), 3)
    for i in quotes_index:
        randomized_quotes.append(quotes[i])
    return randomized_quotes


def generate_url_slug(headline):
    return slugify(headline)
