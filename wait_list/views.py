from rest_framework.generics import CreateAPIView
from .models import WaitList
from .serializers import WaitListSerializer


class WaitListCreateAPIView(CreateAPIView):
    queryset = WaitList.objects.all()
    serializer_class = WaitListSerializer
