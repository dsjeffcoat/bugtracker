from django.db import models
from django.utils import timezone
from myusers.models import CustomUser

# Create your models here.


class BugTicket(models.Model):
    NEW = 'N'
    IN_PROGRESS = 'P'
    DONE = 'D'
    INVALID = 'I'

    TICKET_STATUS_CHOICES = [
        (NEW, 'New'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid'),
    ]

    title = models.CharField(max_length=150)
    time_filed = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    submitted_by = models.ForeignKey(
        CustomUser, related_name="submitted_by", on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=1, choices=TICKET_STATUS_CHOICES, default=NEW)
    assigned_to = models.ForeignKey(
        CustomUser, related_name="assigned_to", on_delete=models.CASCADE, null=True)
    completed_by = models.ForeignKey(
        CustomUser, related_name="completed_by", on_delete=models.CASCADE, null=True)
