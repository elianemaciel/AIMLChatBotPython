from django.db import models
from django.utils import timezone

class Dialog(models.Model):
    owner = models.ForeignKey('auth.User', verbose_name="Dialog owner", related_name="selfDialogs",
                              on_delete=models.CASCADE)


class Message(models.Model):
    dialog = models.ForeignKey(Dialog, verbose_name="Dialog", related_name="messages", on_delete=models.CASCADE)
    sender = models.ForeignKey('auth.User', verbose_name="Author", related_name="messages",
                               on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(verbose_name=("Message text"))
    data = models.DateTimeField(
        default=timezone.now
    )