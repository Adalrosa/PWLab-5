import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class MagicLinkToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def is_valid(self):
        time_elapsed = timezone.now() - self.created_at
        return not self.is_used and time_elapsed.total_seconds() < 900