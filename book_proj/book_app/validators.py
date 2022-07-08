from django.core.exceptions import ValidationError
import datetime
def visit_term_validator(time):
    if time.minute != 0:
        raise ValidationError("this is not a valid format, for example 9:00, 10:00")

def visit_day_validator(day):
    if day <= datetime.datetime.now().date():
        raise ValidationError('You have to choose the future date')