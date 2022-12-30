from django.db import models
from django.contrib.auth.models import User
from .validators import *
# Create your models here.
class Visit(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    Day=models.DateField(validators=[visit_day_validator])
    Term=models.TimeField(null=True, validators=[visit_term_validator])
    Visit_length=models.FloatField(null=False)