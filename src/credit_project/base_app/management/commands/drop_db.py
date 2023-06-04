from django.core.management import BaseCommand

from base_app import models


class Command(BaseCommand):
    def handle(self, car=None, *args, **kwargs):
        models.Producer.objects.all().delete()
        models.Contract.objects.all().delete()
        models.CreditRequest.objects.all().delete()
        models.Product.objects.all().delete()
