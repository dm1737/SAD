import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class NumberValidator(object):
    def validate(self, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit, 0-9."
        )

class LetterValidator(object):
    def validate(self, password, user=None):
        firstChar = password[0]
        print(firstChar)
        if not re.findall('[a-zA-Z]', firstChar):
            raise ValidationError(
                _("The password must start with a letter, A-Z."),
                code='password_no_letter',
            )

    def get_help_text(self):
        return _(
            "Your password must start with a letter, A-Z."
        )
class SpecialValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[^a-zA-Z0-9]', password):
            raise ValidationError(
                _("The password must contain at least 1 special character"),
                code='password_no_letter',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 special character"
        )
