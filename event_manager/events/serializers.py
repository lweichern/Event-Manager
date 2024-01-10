# Serializers are used to convert python data types into JSON

from .models import Tasks
from .models import Events
from rest_framework.serializers import ModelSerializer

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"

class EventSerializer(ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Events
        fields = "__all__"
