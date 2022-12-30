from django.db import models
from django.contrib.auth.models import User
from .validators import *
# Create your models here.
VISIT_LENGTH_CHOICES=(
    (1.0,'1h'),
    (1.5,'1h 30min'),
    (2.0,'2h'),
    )

class Visit(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    Day=models.DateField(validators=[visit_day_validator])
    Term=models.TimeField(null=True, validators=[visit_term_validator])
    Visit_length=models.FloatField(null=True,choices=VISIT_LENGTH_CHOICES,max_length=2)
    Combined_id=models.IntegerField(null=True,blank=True)