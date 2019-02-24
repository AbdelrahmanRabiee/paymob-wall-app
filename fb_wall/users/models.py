from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMessage
from django.conf import settings

from fb_wall.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('email address'), unique=True, db_index=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    middle_name = models.CharField(
        _('middle name'), max_length=255, blank=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between."""
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    def send_template_email(self, template_id, merge_data=None):
        """Send a SendGrid template email."""

        message = EmailMessage(
            subject=None,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[self.email],
            cc=[settings.SERVER_EMAIL]
        )
        message.template_id = template_id
        if merge_data is None:
            merge_data = {
                self.email: {
                    '%first_name%': self.first_name,
                }}
        message.merge_data = merge_data

        message.send()
