from django.urls import path
from .views import JobList, JobDetailView,JobTypeView


urlpatterns = [
    path('', JobList.as_view()),
    path('<int:id>', JobDetailView.as_view()),
    path('category', JobTypeView.as_view()),
]
