from django.db import models


class BaseModel(models.base):
    date_of_creation = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Contract(BaseModel):
    number = models.IntegerField(unique=True)


class CreditRequest(BaseModel):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)


class Producer(BaseModel):
    name = models.CharField(max_length=30)


class Product(BaseModel):
    credit_request = models.ForeignKey(CreditRequest, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)


