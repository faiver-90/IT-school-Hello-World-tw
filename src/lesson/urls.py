from django.urls import path

from src.lesson.views import LessonListCreateView, LessonRetrieveUpdateDeleteView

urlpatterns = [
    path("", LessonListCreateView.as_view()),
    path("<int:pk>/", LessonRetrieveUpdateDeleteView.as_view()),
]