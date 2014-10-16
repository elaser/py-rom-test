from django.db import models
from decimal import Decimal

import rom


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


class FastUser(rom.Model):
    """
    first_name = rom.String(max_length=100) does not work (got an unexpected keyword argument 'max_length')
    db_index doesn't work
    max_digits doesn't work
    decimal_places doesn't work

    user = FastUser(first_name='Anderthan', last_name='Hsieh', credits=100, lat=37.4242, lng=-122.1381, email='anderthan@doordash.com')
    """
    created_at = rom.DateTime()
    updated_at = rom.DateTime()

    first_name = rom.String()
    last_name = rom.String()

    credits = rom.Integer(default=0)

    is_active = rom.Boolean(default=True)

    lat = rom.Float(default=Decimal('0.0'))
    lng = rom.Float(default=Decimal('0.0'))

    email = rom.Text(unique=True)
