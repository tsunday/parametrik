from django.urls import path

from drawings import views

urlpatterns = [
    path("projection/", views.ProjectionCreateView.as_view()),
]
