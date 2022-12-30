from django.core.exceptions import ValidationError
import datetime
LIST_OF_HOURS=[]
for i in range(7,15):
    LIST_OF_HOURS+=[datetime.time(i,0,0)]


def visit_term_validator(time):
    if time.minute != 0:
        raise ValidationError('this is not a valid format, for example 9:00, 10:00')
    if time not in LIST_OF_HOURS:
        raise ValidationError('Choose visit between 7:00-14:00')

def visit_day_validator(day):
    if day <= datetime.datetime.now().date():
        raise ValidationError('You have to choose the future date')