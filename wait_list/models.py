from django.db import models
from django.core.validators import RegexValidator, EmailValidator

email_validator = EmailValidator()

phone_regex = RegexValidator(
    regex=r"^\d{10}", message="Phone number must be 13 digits only!"
)


class WaitList(models.Model):
    USER_TYPE_CHOICES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
    )

    SELLER_TYPE_CHOICES = (
        ('farmer', 'Farmer'),
        ('private_business', 'Private Business'),
    )

    BUYER_TYPE_CHOICES = (
        ('consumer', 'Consumer'),
        ('private_business', 'Private Business'),
    )

    email = models.EmailField(
        max_length=255, unique=True, validators=[email_validator])
    phone_number = models.CharField(
        max_length=30, unique=True, blank=True, null=True, validators=[phone_regex])
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    seller_type = models.CharField(
        max_length=20, choices=SELLER_TYPE_CHOICES, blank=True, null=True)
    buyer_type = models.CharField(
        max_length=20, choices=BUYER_TYPE_CHOICES, blank=True, null=True)
