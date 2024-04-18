from django.db import models


class student(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default= None)
    phone_number = models.SmallIntegerField,
    grade = models.SmallIntegerField( default=1)
    major = models.CharField(max_length=50, default=None)
    password = models.CharField(max_length=200,default=0000, null=False, blank=False)

    def __str__(self) -> str:
        return self.full_name + ' : ' + self.major


