from django.db import models


class User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    credits = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)

    lat = models.DecimalField(max_digits=15, decimal_places=10, default=Decimal('0.0'))
    lng = models.DecimalField(max_digits=15, decimal_places=10, default=Decimal('0.0'))

    email = models.EmailField(max_length=255, unique=True, db_index=True)
