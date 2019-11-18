from django.db import models
from django.utils import timezone

import uuid

# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id = models.AutoField(primary_key=True)
    changed_at = models.DateTimeField(verbose_name='Last modified', db_index=True, blank=True, null=True)

    class Meta:
        abstract = True

    def save_without_updating_timestamp(self, *args, **kwargs):
        return super(BaseModel, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        self.changed_at = timezone.now()

        if kwargs.get("update_fields"):
            arg = tuple(kwargs["update_fields"])

            if "changed_at" not in arg:
                arg = arg + ("changed_at",)
            kwargs["update_fields"] = arg

        return super(BaseModel, self).save(*args, **kwargs)


class Todo(BaseModel):
    # todo title
    title = models.CharField(max_length=255, null=False)
    # description of the task
    task = models.CharField(max_length=255, null=False)
    # task status
    done = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.task)