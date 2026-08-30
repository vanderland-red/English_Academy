from django.shortcuts import render
from django.views import View
from .models import Course
from .models import Enrollment


class CourseDetailView(View):

    def get(self, request, course_id):

        course = Course.objects.get(
            id=course_id,
            is_active=True
        )
        

        return render(request, "course.html", {'course': course})
































# class BuyCourseView(LoginRequiredMixin, View):

#     def get(self, request, course_id):

#         course = Course.objects.get(
#             id=course_id,
#             is_active=True
#         )

#         enrollment = Enrollment.objects.create(
#             user=request.user,
#             course=course,
#             is_paid=False
#         )

#         # اینجا باید کاربر را به درگاه پرداخت بفرستی
