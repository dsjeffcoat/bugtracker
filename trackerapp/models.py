from django.db import models
from django.utils import timezone
from myusers.models import CustomUser

# Create your models here.


class UserProfile(models.Model):
    display_name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.display_name


class BugTicket(models.Model):
    NEW = 'New'
    IN_PROGRESS = 'In Progress'
    DONE = 'Done'
    INVALID = 'Invalid'

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
        CustomUser, related_name="submitted_by", on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=TICKET_STATUS_CHOICES, default=NEW)
    assigned_to = models.ForeignKey(
        CustomUser, related_name="assigned_to", on_delete=models.CASCADE, null=True, blank=True)
    completed_by = models.ForeignKey(
        CustomUser, related_name="completed_by", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
