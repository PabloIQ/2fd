from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
import random
# Create your models here.


class CustmUser(AbstractUser):
    number = models.CharField(max_length=8)


class Code(models.Model):
    number = models.CharField(max_length=8, blank=True)
    user = models.OneToOneField(CustmUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_string = "".join(str(item) for item in code_items)
        self.number = code_string
        super().save(*args, **kwargs)