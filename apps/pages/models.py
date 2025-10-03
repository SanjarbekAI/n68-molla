from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models import CharField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ContactModel(BaseModel):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=15, null=True, blank=True
    )
    subject = models.CharField(
        max_length=255, null=True, blank=True
    )
    message = models.TextField()

    is_read = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        permissions = [
            ("can_change_status", "Can change contact status"),
        ]


class BannerModel(BaseModel):
    image = models.ImageField(upload_to='banners/')
    title = CharField(max_length=256)
    description = RichTextUploadingField()
    text = CharField(max_length=128)
    url = models.URLField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'
