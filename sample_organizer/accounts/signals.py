from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Executor

def executor_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='executor')
        instance.groups.add(group)
        Executor.objects.create(
            user=instance,
            first_name=instance.username,
        )

post_save.connect(executor_profile, sender=User)