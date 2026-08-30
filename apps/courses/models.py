from django.db import models
from apps.accounts.models import User


# دوره
class Course(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'courses'



# ثبت نام کاربر در دوره
class Enrollment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        db_table = 'enrollments'