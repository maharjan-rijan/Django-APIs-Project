from rest_framework import serializers
from students.models import Student, Address, Education

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
    
    address = AddressSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
