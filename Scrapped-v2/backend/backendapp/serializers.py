from django.db import models
from django.db.models import fields
from rest_framework_simplejwt import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import request, serializers
from .models import Committee, DepartmentHead, Teacher, User
from django.contrib.auth import authenticate


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['user_type'] = user.user_type
        return token

class CommitteeRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True
    )

    token = serializers.CharField(max_length = 255, read_only=True)
    class Meta:
        model = Committee
        fields = '__all__'
    
    def create(self, validated_data):
        return Committee.objects.create_committee(**validated_data)

class TeacherRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True
    )

    token = serializers.CharField(max_length = 255, read_only=True)
    class Meta:
        model = Teacher
        fields = ['email','password','initials','token','first_name','last_name','created_by']
    
    def create(self, validated_data):
        return Teacher.objects.create_teacher(**validated_data)

class HeadRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True
    )

    token = serializers.CharField(max_length = 255, read_only=True)
    class Meta:
        model = DepartmentHead
        fields = ['email','password','initials','token','first_name','last_name']
    
    def create(self, validated_data):
        return DepartmentHead.objects.create_head(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
 
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)
 
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            userObj = Teacher.objects.get(email=user.email)
        except Teacher.DoesNotExist:
            userObj = None 
 
        try:
            if userObj is None:
                userObj = Committee.objects.get(email=user.email)
        except Committee.DoesNotExist:
            userObj = None       
 
        try:
            if userObj is None:
                userObj = DepartmentHead.objects.get(email=user.email)
        except DepartmentHead.DoesNotExist:
            raise serializers.ValidationError(
                'No User with given email and password does not exists'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'email': user.email,
            'token': user.token
        }






        
# class CommitteeSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(min_length=6, write_only=True)
#     first_name = serializers.CharField(max_length=150, required = False)
#     last_name = serializers.CharField(max_length=150, required = False)
    
#     id = serializers.CharField(max_length= 150, required=True)
#     session = serializers.CharField(max_length = 20, required=False)
#     external = serializers.CharField(max_length = 200, required=False )
#     created_by = serializers.RelatedField(source='department_head')
#     id = serializers.CharField(max_length= 150, required=True)
    
#     class Meta:
#         model = Committee
#         fields = "__all__"

#     def create(self, validated_data):
#         return Committee.objects.create_committee(**validated_data)


# class TeacherRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=128, min_length=8, write_only=True)

#     token = serializers.CharField(max_length=255, read_only=True)

#     class Meta:
#         model = Teacher
#         fields = [
#             "email",
#             "password",
#             "initials",
#             "token",
#             "first_name",
#             "last_name",
#             "created_by",
#         ]

#     def create(self, validated_data):
#         return Teacher.objects.create_teacher(**validated_data)


# class HeadRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=128, min_length=8, write_only=True)

#     token = serializers.CharField(max_length=255, read_only=True)

#     class Meta:
#         model = DepartmentHead
#         fields = ["email", "password", "initials", "token", "first_name", "last_name"]

#     def create(self, validated_data):
#         return DepartmentHead.objects.create_head(**validated_data)


# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=255)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)

#     def validate(self, data):
#         email = data.get("email", None)
#         password = data.get("password", None)
#         user = authenticate(username=email, password=password)

#         if user is None:
#             raise serializers.ValidationError(
#                 "A user with this email and password is not found."
#             )
#         try:
#             userObj = Teacher.objects.get(email=user.email)
#         except Teacher.DoesNotExist:
#             userObj = None

#         try:
#             if userObj is None:
#                 userObj = Committee.objects.get(email=user.email)
#         except Committee.DoesNotExist:
#             raise serializers.ValidationError(
#                 "User with given email and password does not exists"
#             )

#         try:
#             if userObj is None:
#                 userObj = DepartmentHead.objects.get(email=user.email)
#         except DepartmentHead.DoesNotExist:
#             raise serializers.ValidationError(
#                 "User with given email and password does not exists"
#             )

#         if not user.is_active:
#             raise serializers.ValidationError("This user has been deactivated.")

#         return {"email": user.email, "token": user.token}


# # class CommitteeSerializer(serializers.ModelSerializer):
# #     email = serializers.EmailField(required=True)
# #     password = serializers.CharField(min_length=6, write_only=True)
# #     first_name = serializers.CharField(max_length=150, required = False)
# #     last_name = serializers.CharField(max_length=150, required = False)

# #     id = serializers.CharField(max_length= 150, required=True)
# #     session = serializers.CharField(max_length = 20, required=False)
# #     external = serializers.CharField(max_length = 200, required=False )
# #     created_by = serializers.RelatedField(source='department_head')
# #     id = serializers.CharField(max_length= 150, required=True)

# #     class Meta:
# #         model = Committee
# #         fields = (
# #             'username',
# #             'email',
# #             'password',
# #             'first_name',
# #             'last_name',
# #             'designation'
# #         )
# #         extra_kwargs = {
# #             'password': {
# #                 'write_only': True
# #             }
# #         }

# #     def create(self, validated_data):
# #         password = validated_data.pop('password', None)
# #         instance = self.Meta.model(**validated_data)
# #         if password is not None:
# #             instance.set_password(password)
# #         instance.save()
# #         return instance

# # class TeacherSerializer(serializers.ModelSerializer):
# #     username = serializers.CharField(min_length=2, max_length=3, required=True)
# #     email = serializers.EmailField(required=True)
# #     password = serializers.CharField(min_length=6, write_only=True)
# #     first_name = serializers.CharField(max_length=150, required = False)
# #     last_name = serializers.CharField(max_length=150, required = False)
# #     designation = serializers.CharField(max_length=20, required = False)

# #     class Meta:
# #         model = User
# #         fields = (
# #             'username',
# #             'email',
# #             'password',
# #             'first_name',
# #             'last_name',
# #             'designation'
# #         )
# #         extra_kwargs = {
# #             'password': {
# #                 'write_only': True
# #             }
# #         }

# #     def create(self, validated_data):
# #         password = validated_data.pop('password', None)
# #         instance = self.Meta.model(**validated_data)
# #         if password is not None:
# #             instance.set_password(password)
# #         instance.save()
# #         return instance

# # class HeadSerializer(serializers.ModelSerializer):
# #     username = serializers.CharField(min_length=2, max_length=3, required=True)
# #     email = serializers.EmailField(required=True)
# #     password = serializers.CharField(min_length=6, write_only=True)
# #     first_name = serializers.CharField(max_length=150, required = False)
# #     last_name = serializers.CharField(max_length=150, required = False)
# #     designation = serializers.CharField(max_length=20, required = False)

# #     class Meta:
# #         model = User
# #         fields = (
# #             'username',
# #             'email',
# #             'password',
# #             'first_name',
# #             'last_name',
# #             'designation'
# #         )
# #         extra_kwargs = {
# #             'password': {
# #                 'write_only': True
# #             }
# #         }

# #     def create(self, validated_data):
# #         password = validated_data.pop('password', None)
# #         instance = self.Meta.model(**validated_data)
# #         if password is not None:
# #             instance.set_password(password)
# #         instance.save()
# #         return instance
