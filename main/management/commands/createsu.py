"""
Create a `python manage.py` command to create an admin superuser
This is for use by Beanstalk when it deploys
"""
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    """ Command for creating a superuser """
    def handle(self, *args, **options):
        if not User.objects.filter(username="cyqlo").exists():
            User.objects.create_superuser("cyqlo", "cyqlo@cyqlo.io", os.environ['RDS_PASSWORD'])
