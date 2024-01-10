from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    # path("", views.getRoutes, name="routes"),
    path("events", views.getEvents, name="events"),
    path("events/<str:pk>", views.getEvent, name="event"),
    path("", include(router.urls)),
    path("events/<int:event_id>/tasks", views.TaskViewSet.as_view({'get': 'by_event'}), name="taks-by-event")
]