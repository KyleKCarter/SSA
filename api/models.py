from django.db import models

# Create your models here.
class Teams(models.Model):
    team_name = models.CharField(max_length=200, default='', unique=True)
    league = models.CharField(max_length=100, default='')
    avg_score = models.DecimalField(max_digits=10, decimal_places=3, null=False, default=1)
    opp_avg_score = models.DecimalField(max_digits=10, decimal_places=3, null=False, default=1)