from rest_framework import serializers
from .models import Teacher, User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ["email", "password"]

    def create(self, validated_data):
        user = User.objects.create(  # this line  will solve your problem
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Teacher
        fields = [
            "user",
            "initials",
            "name",
            "is_dept_head",
        ]

    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher
