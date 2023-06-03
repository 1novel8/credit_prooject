from django.db import models


class BaseModel(models.base):
    date_of_creation = models.DateField(auto_now_add=True)
