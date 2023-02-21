from django.contrib.auth.models import User
from django.db import models

TEXT_MAX_LENGTH = 255


class TodoItem(models.Model):
    title = models.CharField(max_length=TEXT_MAX_LENGTH)
    description = models.TextField()
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        verbose_name='createdAt', auto_now_add=True
    )
    updated_at = models.DateTimeField(verbose_name='updatedAt', auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
