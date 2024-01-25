from django.db import models
from datetime import datetime


class IhaData(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Stock = models.IntegerField()
    YearUnitFee = models.FloatField()
    Currency = models.CharField(max_length=50, default="₺")
    IsForRent = models.BooleanField(default=False)
    IsDelete = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.IsDelete = True
        self.save()
    
    def save(self, *args, **kwargs):
        if self.Stock == 0:
            self.IsForRent = False
        else:
            self.IsForRent = True
        super().save(*args, **kwargs)
        

class UserWindowIha(models.Model):
    Id = models.AutoField(primary_key=True)
    IhaId = models.ForeignKey(
        IhaData,
        on_delete=models.SET_NULL,
        limit_choices_to={"IsForRent": True, "IsDelete": False},
        null=True,
    )
    PurpchaseDate = models.IntegerField(default=datetime.now().year)
    PurpchaseEndDate = models.IntegerField()
    PurpchaseQuantity = models.IntegerField(default=0)
    TotalFee = models.FloatField(default=0)
    Currency = models.CharField(max_length=50, default="₺", editable=False)


class CustomUser(models.Model):
    Id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Is_Admin = models.BooleanField(default=0)
