from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Action(models.Model):

    VERB_CHOICES = (
        ("is following", "is following"),
        ("bookmarked image", "bookmarked image"),
        ("liked", "liked"),
        ("has joined the platform", "has joined the platform"),
    )

    target_content_type_limit = models.Q(app_label__in=["account", "actions", "images"])

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(get_user_model(), related_name="actions", db_index=True, on_delete=models.CASCADE)
    verb = models.CharField(max_length=150, choices=VERB_CHOICES)
    target_content_type = models.ForeignKey(ContentType, limit_choices_to=target_content_type_limit, related_name="target_objects", blank=True, null=True, on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(blank=True, null=True, db_index=True)
    target = GenericForeignKey("target_content_type", "target_id")

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.id)

