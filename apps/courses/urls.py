from django.urls import path
from . import views



app_name = 'course'
urlpatterns = [
    path('detail/<int:course_id>/', views.CourseDetailView.as_view(), name='detail'),
    path('buy/<int:course_id>/', views.BuyCourseView.as_view(), name='buy'),
    path('payment/<int:enrollment_id>/', views.PaymentView.as_view(), name='payment'),
]