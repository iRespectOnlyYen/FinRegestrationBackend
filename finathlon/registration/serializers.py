from rest_framework import serializers

from . models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'last_name', 'first_name', 'middle_name', 'date_of_birth', 'place_of_birth', 'residence_index',
                  'residence_address', 'phone_number', 'email', 'additional_json_data', 'cat']
