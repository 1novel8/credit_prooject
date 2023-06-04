import random

from django.core.management import BaseCommand

from base_app import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        producer_list = list()
        contract_list = list()
        credit_request_list = list()

        for i in range(50):
            contract = self.create_contract(i)
            contract_list.append(contract)

            credit_request = self.create_credit_request(contract)
            credit_request_list.append(credit_request)

            for j in range(10):
                if random.randint(0, 2) == 1:
                    continue
                producer = self.create_producer(i*100+j*10)
                producer_list.append(producer)

                for z in range(10):
                    if random.randint(0, 2) == 1:
                        continue
                    product = self.create_product(i*100+j*10+z, producer, credit_request)

    @staticmethod
    def create_producer(index):
        producer = models.Producer.objects.create(
            name=f'nick_{index}'
        )
        return producer

    @staticmethod
    def create_contract(index):
        contract = models.Contract.objects.create(
            number=index
        )
        return contract

    @staticmethod
    def create_credit_request(contract):
        credit_request = models.CreditRequest.objects.create(
            contract=contract
        )
        return credit_request

    @staticmethod
    def create_product(index, producer, credit_request):
        product = models.Product.objects.create(
            name=f'product_{index}',
            producer=producer,
            credit_request=credit_request
        )
        return product
