import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from general.models import Country


class User(AbstractUser):
    id = models.UUIDField(unique=True, primary_key=True,editable=False, default=uuid.uuid4)
    is_deleted = models.BooleanField(default=False)

    email = models.EmailField(unique=False,null=True, blank=True)
    encrypted_password = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        db_table = 'users_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-date_joined',)

    def __str__(self):
        return self.username