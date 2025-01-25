from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics
from .serializers import TeamSerializer
from .models import Teams

# Create your views here.
# def main(request):
#     return HttpResponse("Sports Statistics App")

class TeamAdd(generics.CreateAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer

class TeamsView(generics.ListAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer