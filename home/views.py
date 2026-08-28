from django.shortcuts import render, get_object_or_404
from apps.courses.models import Course

def about(requset):
    return render(requset, "about.html")

# نمایش پکیج ها در صفحه اصلی
def home(request):
    courses = Course.objects.filter(is_active=True)

    return render(request, 'home.html', {'courses': courses}) # ارسال اطلاعات به صفحه اصلی

