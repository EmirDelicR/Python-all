from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

import uuid
from . import choices

# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Last modified', db_index=True, auto_now=True)

    class Meta:
        ordering = ["created_at"]
        abstract = True

    # def save_without_updating_timestamp(self, *args, **kwargs):
    #     return super(BaseModel, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     """ On save, update timestamps """
    #     self.changed_at = timezone.now()

    #     if kwargs.get("update_fields"):
    #         arg = tuple(kwargs["update_fields"])

    #         if "changed_at" not in arg:
    #             arg = arg + ("changed_at",)
    #         kwargs["update_fields"] = arg

    #     return super(BaseModel, self).save(*args, **kwargs)


class Address(BaseModel):
    country = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    street = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        # f"" is short way to format string
        return f"{self.city}"


class User(AbstractUser):
    status = models.PositiveSmallIntegerField(choices=choices.USER_STATUS, default=1)
    
    address = models.OneToOneField(
        'Address', verbose_name="user address", on_delete=models.SET_NULL, null=True, blank=True, related_name='user'
    )

    def __str__(self):
        # f"" is short way to format string
        return f"{self.username}"


class Todo(BaseModel):
    # todo title
    title = models.CharField(max_length=255, null=False)
    # description of the task
    task = models.CharField(max_length=255, null=False)
    # task status
    done = models.BooleanField(default=False)
    
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='todo')

    def __str__(self):
        # f"" is short way to format string
        return f"{self.title} - {self.task}"


# This is model for relation serilizer
# class FirewallChain(BaseModel):
#     spi_box = models.ForeignKey(
#         'SPIBox',
#         related_name='firewall_chains',
#         on_delete=models.CASCADE
#     )
#     name = models.CharField(max_length=255)
#     template = models.ForeignKey(
#         'FirewallTemplate',
#         related_name='firewall_chain',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL
#     )
#     machine = models.OneToOneField(
#         Machine,
#         related_name='firewall_chain',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL
#     )
#     rules = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.name}"

# class FirewallVariable(BaseModel):
#     name = models.CharField(max_length=255)
#     value = models.CharField(max_length=512)
#     firewall_template = models.ForeignKey(
#         'FirewallTemplate', related_name='firewall_variables', null=True, blank=True, on_delete=models.CASCADE
#     )
#     firewall_chain = models.ForeignKey(
#         'FirewallChain', related_name='firewall_variables', null=True, blank=True, on_delete=models.CASCADE
#     )