from getpass import getpass

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from mailadmin.models import UserAdditions


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--username', default=None)
        parser.add_argument('--password', default=None)

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        if not (username or password):
            try:
                self.stdout.write('Create admin user for you MailAdmin installation:')
                default_user_name = 'admin'
                username = str(input('Username [%s]: ' % default_user_name)).strip() or default_user_name
                password = str(getpass('Password: '))
            except (KeyboardInterrupt, EOFError):
                print()
                return
        try:
            User.objects.get(username__exact=username)
            self.stdout.write(self.style.ERROR('User with name %s does already exist.' % username))
        except ObjectDoesNotExist:
            user = User()
            user.username = username
            user.set_password(password)
            user.save()

            useradditions = UserAdditions()
            useradditions.user = user
            useradditions.roles = 4
            useradditions.save()

            self.stdout.write(self.style.SUCCESS('Admin user %s created.' % username))
