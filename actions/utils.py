from .models import Action
from django.utils import timezone
from datetime import timedelta
from django.contrib.contenttypes.models import ContentType

def register_action(user, verb, target=None):
    last_hour_ago = timezone.now() - timedelta(hours=1)
    similar_actions = Action.objects.filter(user=user, verb=verb, created__gte=last_hour_ago)

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_id=target.id, target_content_type=target_ct)

    if similar_actions.count() == 0:
        Action.objects.create(user=user, verb=verb, target=target)
        return True

    return False