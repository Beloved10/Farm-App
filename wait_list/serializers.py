from rest_framework import serializers
from .models import WaitList


class WaitListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitList
        fields = '__all__'


class WaitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitList
        fields = ['id', 'email', 'phone_number',
                  'user_type', 'seller_type', 'buyer_type']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        user_type = representation['user_type']
        if user_type == 'seller':
            # If the user is a seller, remove buyer_type
            representation.pop('buyer_type', None)
        elif user_type == 'buyer':
            # If the user is a buyer, remove seller_type
            representation.pop('seller_type', None)

        return representation
