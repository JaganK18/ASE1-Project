from django.db import models

# Create your models here.
class Orders_Buying(models.Model):
    Products_Selling = models.ForeignKey("Products_Selling", on_delete=models.CASCADE)
    Buyer = models.ForeignKey("login.Profile", on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now=True)
    isConfirmed = models.BooleanField(default=False)
    amount = models.FloatField(null=False)