from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import Comment


class CommentView(View):
    """
    View for comment POST requests.
    A 'get' method could be added for rendering
    context and the comments.html form partial could be updated
    to improve this view
    """

    template_name = 'comments/comments.html'

    def post(self, request, article_uuid):
        text = self.request.POST.get('comment', "")
        new_comment = Comment(
            uuid=article_uuid,
            text=text
        )
        new_comment.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
 