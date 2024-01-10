from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .utils import getEventLists, getEventDetail, createEvent, updateEvent, deleteEvent
from .models import Tasks
from .serializers import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def by_event(self, request, event_id=None):
        tasks = Tasks.objects.filter(event=event_id)
        serializer = self.get_serializer(tasks, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def getRoutes(request):
    return Response("Hello Worllld") 

@api_view(['GET', 'POST'])
def getEvents(request):
    if request.method == "GET":
        return getEventLists(request)
    
    if request.method == "POST":
        return createEvent(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getEvent(request, pk):
    if request.method == "GET":
        return getEventDetail(pk)
    
    if request.method == "PUT":
        return updateEvent(request, pk)
    
    if request.method == "DELETE":
        return deleteEvent(request, pk)
