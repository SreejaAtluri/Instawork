from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField


class Adddata(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField('First Name', max_length=200)
    lastname = models.CharField('Last Name', max_length=200)
    email = models.EmailField('Email', unique=True)
    phoneNumber = PhoneNumberField(unique=True, null=False, blank=False)
    ROLE_CHOICES = [(1, mark_safe(u'<em>Admin</em> - Can delete members')), (2, mark_safe(u'<em>Regular</em> - Cannot delete members'))]
    role = models.PositiveIntegerField(choices=ROLE_CHOICES, default=2)

    def __str__(self):
        return f"{self.firstname}"

    def get_absolute_url(self):
        return reverse("Instaworkapp:listview")
