from rest_framework import serializers
from .models import * 

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('id','first_name','last_name','phone',)

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ('id','contributions','parents',)
        