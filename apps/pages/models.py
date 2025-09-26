from django.db import models


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


class TeamModel(BaseModel):
    image = models.ImageField(upload_to='team/')
    full_name = models.CharField(max_length=128)
    position = models.CharField()

    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'