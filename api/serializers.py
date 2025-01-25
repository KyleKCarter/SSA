from rest_framework import serializers
from .models import Teams

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ('id', 'team_name', 'league', 'avg_score', 'opp_avg_score')