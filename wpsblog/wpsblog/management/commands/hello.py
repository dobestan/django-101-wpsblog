from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("hello world")
