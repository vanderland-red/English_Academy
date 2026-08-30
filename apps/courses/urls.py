from django.urls import path
from . import views



app_name = 'course'
urlpatterns = [
    path('detail/<int:course_id>/', views.CourseDetailView.as_view(), name='detail'),
]