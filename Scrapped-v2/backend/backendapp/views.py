# from .renderers import UserJSONRenderer
# from rest_framework import permissions, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializers import (
#     CommitteeRegistrationSerializer,
#     HeadRegistrationSerializer,
#     TeacherRegistrationSerializer,
#     UserLoginSerializer,
# )

# from django.http import HttpResponse

# # class ObtainTokenPairWithTypeView(TokenObtainPairView):
# #     permission_classes = (permissions.AllowAny,)
# #     serializer_class = MyTokenObtainPairSerializer


# class CommitteeCreate(APIView):
#     permission_classes = (permissions.AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = CommitteeRegistrationSerializer

#     def post(self, request, format="json"):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class TeacherCreate(APIView):
#     permission_classes = (permissions.AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = TeacherRegistrationSerializer

#     def post(self, request, format="json"):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class HeadCreate(APIView):
#     permission_classes = (permissions.AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = HeadRegistrationSerializer

#     def post(self, request, format="json"):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class UserLogin(APIView):
#     permission_classes = (permissions.AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = UserLoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class HelloWorld(APIView):
#     def get(self, request):
#         return Response(data={"Hello": "World"}, status=status.HTTP_200_OK)
