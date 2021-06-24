from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=40,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = None
    last_name = None
    full_name = models.CharField(_('full_name'), max_length=255, blank=True)

    avatar = models.URLField(blank=True)

    email = models.EmailField(_('email address'), unique=True)
    address = models.CharField(_('address'), max_length=500)
    year_birth = models.PositiveSmallIntegerField(null=True, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.username

