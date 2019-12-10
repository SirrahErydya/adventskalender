from django.core.management.base import BaseCommand
from app.models import Config, Window
import os


class Command(BaseCommand):
    help = 'Closes all open windows'

    def handle(self, *args, **options):
        for window in Window.objects.all():
            window.open = False
            window.save()
