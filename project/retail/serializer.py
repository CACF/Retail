from rest_framework import serializers

from .models import Customer

class customer_serializer(serializers.ModelSerializer):
    customer_id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=True)
    contact_information=serializers.CharField(required=True)
    address=serializers.CharField(required=True)
    class Meta:
        model =  Customer
        fields = "__all__"