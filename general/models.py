import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True,null=True,blank=True)
    creator = models.ForeignKey("users.User", related_name="creator_%(class)s_objects", on_delete=models.CASCADE,null=True,blank=True)
    updater = models.ForeignKey("users.User", related_name="updator_%(class)s_objects", on_delete=models.CASCADE,null=True,blank=True)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Mode(models.Model):
    readonly = models.BooleanField(default=False)
    maintenance = models.BooleanField(default=False)
    down = models.BooleanField(default=False)

    class Meta:
        db_table = 'mode'
        verbose_name = _('mode')
        verbose_name_plural = _('mode')
        ordering = ('id',)

    def __str__(self):
        return str(self.id)
    

class Country(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    web_code = models.CharField(max_length=128, null=True, blank=True)
    country_code = models.CharField(max_length=128, null=True)
    phone_code = models.CharField(max_length=128, null=True, blank=True)
    phone_number_length = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    flag = models.ImageField(upload_to="countries/flags/", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'general_country'
        verbose_name = _('country')
        verbose_name_plural = _('countries')
        ordering = ('name',)

    def __str__(self):
        return self.name