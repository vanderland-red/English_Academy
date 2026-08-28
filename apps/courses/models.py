from django.db import models

from django.db import models


class Course(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'courses'