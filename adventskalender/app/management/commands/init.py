from django.core.management.base import BaseCommand
from app.models import Config, Window
import os


class Command(BaseCommand):
    help = 'Create the initial database entries for all 24 windows'

    def handle(self, *args, **options):
        conf = Config.load()
        conf.background.name = 'stars_background.jpg'
        conf.save()
        for i in range(1, 25):
            window = Window(day=i, open=False)
            window.content.name = os.path.join('window_contents', 'placeholder.jpg')
            window.save()
