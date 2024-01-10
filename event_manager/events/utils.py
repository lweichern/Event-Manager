
from rest_framework.response import Response
from rest_framework import status
from .models import Events
from .serializers import EventSerializer

# Create your views here.

def getRoutes(request):
    return Response("Hello Worllld") 

def getEventLists(request):
    events = Events.objects.all()
    # Need serializer to convert python data to json format
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

def getEventDetail(pk):
    # event = Events.objects.get(id=pk)
    # Need serializer to convert python data to json format
    try:
        event = Events.objects.get(id=pk)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

def createEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def updateEvent(request, pk):
    data = request.data
    event = Events.objects.get(id=pk)
    serializer = EventSerializer(event, data=data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteEvent(request, pk):
    try:
        event = Events.objects.get(id=pk)
    except Events.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    event.delete()
    return Response(status.HTTP_200_OK)   
