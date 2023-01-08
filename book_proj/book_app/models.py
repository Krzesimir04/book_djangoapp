from django.db import models
from django.contrib.auth.models import User
from .validators import *
# Create your models here.
class Visit(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    Day=models.DateField(validators=[visit_day_validator])
    Term=models.TimeField(null=True)
    Visit_length=models.FloatField(null=False)

    def __str__(self):
        if self.User is not None:
            return f'{self.User}, day: {self.Day}, hour: {self.Term}'
        return f'{self.id}'