from django.urls import path
from .views import TeamsView, TeamAdd

urlpatterns = [
    path('', TeamAdd.as_view()),
    path('teams', TeamsView.as_view()),

]