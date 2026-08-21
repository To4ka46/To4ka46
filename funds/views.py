from rest_framework import viewsets, permissions
from .models import Collect, Payment
from .serializers import CollectSerializer, PaymentSerializer
from .permissions import IsAuthorOrReadOnly

class CollectViewSet(viewsets.ModelViewSet):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        collect_id = self.kwargs.get("collect_pk")
        collect = Collect.objects.get(pk=collect_id)
        serializer.save(user=self.request.user, collect=collect)
