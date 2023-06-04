from rest_framework import viewsets, routers, mixins, views
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

import base_app.models as models
import base_app.serializers as serializers

router = routers.DefaultRouter()


class CreditRequestView(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = models.CreditRequest.objects.all()
    serializer_class = serializers.CreditRequestSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class ContractView(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class ProductView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class ProducerView(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = models.Producer.objects.all()
    serializer_class = serializers.ProducerSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


@api_view(['GET'])
def query(request, pk):
    response = models.CreditRequest.objects.filter(id=pk)\
                                            .values('product__producer_id')\
                                            .distinct()
    return Response(response)


router.register(prefix='credit_request', viewset=CreditRequestView)
router.register(prefix='contract', viewset=ContractView)
router.register(prefix='product', viewset=ProductView)
router.register(prefix='producer', viewset=ProducerView)
