from rest_framework import serializers

from dummy.models import testform


class TestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = testform
        fields = '__all__' 