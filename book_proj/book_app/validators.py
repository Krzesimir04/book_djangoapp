from django.core.exceptions import ValidationError
import datetime

def visit_day_validator(day):
    if day <= datetime.datetime.now().date():
        raise ValidationError('You have to choose the future date')