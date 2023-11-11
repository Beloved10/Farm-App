from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WaitList
from .serializers import WaitListCreateSerializer, WaitListSerializer


class WaitListCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = WaitListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WaitListView(APIView):
    def get(self, request, *args, **kwargs):
        waitlist_objects = WaitList.objects.all()
        serializer = WaitListSerializer(waitlist_objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
