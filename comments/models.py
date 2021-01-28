import uuid

from django.db import models
# from django.contrib.sessions.models import Session


class Comment(models.Model):
    """ 
    The anonymous comment functionality could be futher extended (comment moderation, 
    notifications, tracking replies) by saving a session with each comment

    """
    # session = models.ForeignKey(Session, blank=True, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text