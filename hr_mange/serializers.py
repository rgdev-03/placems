from rest_framework import serializers
from .models import Batch, Branch, Student, Staff, Certi_Skills, Projects, Achievements, Academic_Per
from django.contrib.auth import get_user_model
User = get_user_model()

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user_data = {
            "username": validated_data['USN'],  # Assuming USN is unique and used as username
            "email": validated_data.get('email'),  # Ensure 'email' is included in Student model or adjusted accordingly
            "password": "rymec@123",  # You should use a better way to handle passwords
            "is_student": True,  # Set is_student to True for student user

        }
        user = User.objects.create_user(**user_data)
        user.save()
        student = Student.objects.create(**validated_data, user=user)
        return student


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

    def create(self, validated_data):
        user_data = {
            "username": validated_data['email'],  # Assuming email is unique and used as username
            "email": validated_data['email'],
            "password": "rymec",  # You should use a better way to handle passwords
            "is_staff_member": True,  # Set is_staff_member to True for staff user
        }
        user = User.objects.create_user(**user_data)
        user.save()
        
        staff = Staff.objects.create(**validated_data, user=user)
        return staff

class Certi_SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certi_Skills
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = '__all__'

class Academic_PerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Per
        fields = '__all__'

