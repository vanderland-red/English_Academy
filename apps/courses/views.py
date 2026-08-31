from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Course, Enrollment, Payment


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

    def post(self, request, enrollment_id):

        enrollment = get_object_or_404(
            Enrollment,
            id=enrollment_id,
            user=request.user,
            is_paid=False
        )

        payment = Payment.objects.create(
            enrollment=enrollment,
            amount=enrollment.course.price
        )

        return redirect('course:mock-payment', payment.authority) # کد تراکنش توی مدل ها تولید میشه خودش




#===================
# Mock Payment Show
#===================
class MockPaymentView(LoginRequiredMixin, View):

    def get(self, request, authority):

        payment = get_object_or_404(
            Payment,
            authority=authority,
            enrollment__user=request.user,
            status='pending'
        )

        return render(
            request,
            'course/mock_payment.html',
            {
                'payment': payment,
                'course': payment.enrollment.course
            }
        )



#================
# Verify Payment
#================
class VerifyPaymentView(LoginRequiredMixin, View):

    def post(self, request, authority):

        payment = get_object_or_404(
            Payment,
            authority=authority,
            enrollment__user=request.user,
            status='pending'
        )

        status = request.POST.get('status')

        if status == 'success':

            payment.status = 'success'
            payment.ref_id = str(payment.id)

            payment.save()

            payment.enrollment.is_paid = True
            payment.enrollment.save()

            messages.success(request,'پرداخت با موفقیت انجام شد.')

            return redirect('user:dashboard')

        elif status == 'failed':

            payment.status = 'failed'
            payment.save()

            messages.error(request,'پرداخت لغو شد.')

            return redirect('course:payment', payment.enrollment.id)

        return redirect('course:mock-payment', payment.authority)