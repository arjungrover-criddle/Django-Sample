from django.db import models
from user.models import UserInfo

# Create your models here.
class StoreInfo(models.Model):
    """
    This model will store details about store
    """
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    store_name = models.CharField(verbose_name="Store Name", max_length=128, blank=False)
    store_address = models.CharField(verbose_name="Store Address", max_length=128, blank=True)

    def __str__(self):
        return "{}:{}".format(self.store_name, self.store_address)
