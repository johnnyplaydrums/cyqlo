from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="cyqlo").exists():
            User.objects.create_superuser("cyqlo", "cyqlo@cyqlo.io", os.environ['RDS_PASSWORD'])
