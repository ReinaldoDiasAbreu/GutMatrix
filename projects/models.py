from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add = True)
    gravity = models.PositiveSmallIntegerField(null=False)
    urgency = models.PositiveSmallIntegerField(null=False)
    trend = models.PositiveSmallIntegerField(null=False)

    objects = models.Manager()  # The default manager.

    def __str__(self) -> str:
        return self.title

