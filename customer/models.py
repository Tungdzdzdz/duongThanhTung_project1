# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    # Các trường khác của Customer

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_groups',  # Thay đổi related_name để tránh xung đột
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_user_permissions',  # Thay đổi related_name để tránh xung đột
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )