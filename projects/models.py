from django.db import models

class ProjectDetails(models.Model):
    title = models.CharField(max_length=100)
    mention = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=400)
    techused = models.CharField(max_length=400, null=True)
    additional_description = models.CharField(max_length = 500, null=True)

class ProjectLinks(models.Model):
    project_id = models.IntegerField(null=True)
    text = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=400, null=True)