from django.core.management.base import BaseCommand, CommandError
from projects.models import Project


class Command(BaseCommand):
    help = 'closes the specified project'

    def add_arguments(self, parser):
        pass
