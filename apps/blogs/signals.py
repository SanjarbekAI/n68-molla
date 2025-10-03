from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from apps.blogs.models import BlogModel


@receiver(post_save, sender=BlogModel)
def post_save_blog_model_signal(sender, instance, created, **kwargs):
    if created:
        print(instance.title)
        print("Signal is working")


@receiver(post_delete, sender=BlogModel)
def post_delete_blog_model_signal(sender, instance, **kwargs):
    print(instance.title)
    print("Deleting signal is working")
