from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Course, Enrollment


#=================
# Choice Course
#=================
class CourseDetailView(View):

    def get(self, request, course_id):

        course = get_object_or_404(Course, id=course_id, is_active=True)

        return render(request, 'course/course.html', {'course': course})



#=================
# Buy Course
#=================
class BuyCourseView(LoginRequiredMixin, View):

    def get(self, request, course_id):

        course = get_object_or_404(Course,id=course_id, is_active=True)

        # اگر کاربر قبلاً این دوره را خریده باشد
        enrollment = Enrollment.objects.filter(user=request.user, course=course).first()

        if enrollment and enrollment.is_paid:
            messages.info(request,'شما قبلاً این دوره را خریداری کرده‌اید.')
            return redirect('user:dashboard')

        # اگر دوره رو نداره پس براش بساز
        if not enrollment:
            enrollment = Enrollment.objects.create(
                user=request.user,
                course=course,
                is_paid=False
            )


        # ارسال به درگاه پرداخت
        return redirect('course:payment', enrollment.id)


#============
# Payment
#============
class PaymentView(LoginRequiredMixin, View):

    def get(self, request, enrollment_id):

        enrollment = get_object_or_404(
            Enrollment,
            id=enrollment_id,
            user=request.user,
            is_paid=False
        )

        return render(request, 'course/payment.html',
            {
                'enrollment': enrollment,
                'course': enrollment.course
            }
        )