from django.db import models


class BlogModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(status="DELETED")

    def all_objects(self):
        return super().get_queryset()

    def published(self):
        return self.get_queryset().filter(status="PUBLISHED")
