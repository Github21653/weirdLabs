from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SaleItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name