from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework import permissions

from django.db import IntegrityError
from .models import Teacher, User
from .serializers import TeacherSerializer, UserSerializer


class TeacherList(generics.ListAPIView):
    """
    Return list of all teachers
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherCreate(generics.CreateAPIView):
    serializer_class = TeacherSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super(generics.CreateAPIView, self).create(request, *args, **kwargs)
        except IntegrityError:
            content = {"error": "IntegrityError. User with email already exists!"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetail(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# class UserCreate(generics.CreateAPIView):
#     """
#     Creates User using email, password
#     Password is stored as hash
#     """

#     serializer_class = UserSerializer

#     def create(self, request, *args, **kwargs):
#         try:
#             return super(generics.CreateAPIView, self).create(request, *args, **kwargs)
#         except IntegrityError:
#             content = {"error": "IntegrityError. User with email already exists!"}
#             return Response(content, status=status.HTTP_400_BAD_REQUEST)
