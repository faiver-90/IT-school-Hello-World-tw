from django.urls import path

from src.student.views import StudentListCreateView, StudentRetrieveUpdateDeleteView

urlpatterns = [
    path("", StudentListCreateView.as_view()),
    path("<int:pk>/", StudentRetrieveUpdateDeleteView.as_view()),
]
