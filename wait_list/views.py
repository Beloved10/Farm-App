from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WaitList
from .serializers import WaitListCreateSerializer, WaitListSerializer


class WaitListCreateAPIView(CreateAPIView):
    queryset = WaitList.objects.all()
    serializer_class = WaitListCreateSerializer


class WaitListView(APIView):
    def get(self, request, *args, **kwargs):
        waitlist_objects = WaitList.objects.all()
        serializer = WaitListSerializer(waitlist_objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
