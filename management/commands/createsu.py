import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        if not User.objects.filter(username="bharani09").exists():
            password = os.environ.get("SUPERUSER_PASSWORD")
            if password is None:
                raise ValueError("Password not found")
            User.objects.create_superuser(
                first_name='bharani',
                last_name='kumar',
                username="bharani09",
                email="bharanikumar070@gmail.com", 
                password='bharani070',
            )
            print("Superuser has been created.")
        else:
            print("Superuser exists")