from rest_framework import serializers
from .models import Student
from django.contrib.auth.hashers import make_password

class StudentSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['id','name','phone_number','password','confirm_password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self,data):

        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")

        return data

    def create(self,validated_data):

        validated_data.pop('confirm_password')

        validated_data['password'] = make_password(validated_data['password'])

        return Student.objects.create(**validated_data)
