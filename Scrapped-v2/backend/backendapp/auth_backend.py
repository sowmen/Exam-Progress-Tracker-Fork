from django.contrib import auth
import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from .models import Committee, DepartmentHead, Teacher, User

# class JWTTeacherAuthentication(authentication.BaseAuthentication):
#     authentication_header_prefix = 'Token'

#     def authenticate(self, request):
#         request.user = None
#         auth_header = authentication.get_authorization_header(request).split()
#         auth_header_prefix = self.authentication_header_prefix.lower()

#         if not auth_header:
#             return None
#         if len(auth_header)==1:
#             return None
#         elif len(auth_header)>2:
#             return None
#         prefix = auth_header[0].decode('utf-8')
#         token = auth_header[1].decode('utf-8')

#         if prefix.lower() != auth_header_prefix:
#             return None
        
#         return self._authenticate_credentials(request, token)
    
#     def _authenticate_credentials(self, request, token):
#         try:
#             print("TOKEN IS:"+token)
#             payload = jwt.decode(jwt=token, key="Deez Nuts", algorithms=['HS256'])
#         except:
#             raise exceptions.AuthenticationFailed("Invalid Authentication. Could not decode teacher token.")

#         try:
#             user = Teacher.objects.get(pk=payload['id'])
#         except Teacher.DoesNotExist:
#             raise exceptions.AuthenticationFailed("No Teacher matching this token was found.")

#         if not user.is_active:
#             raise exceptions.AuthenticationFailed("This User has been deactivated")
        
#         return(user, token)

# class JWTCommitteeAuthentication(authentication.BaseAuthentication):
#     authentication_header_prefix = 'Token'

#     def authenticate(self, request):
#         request.user = None
#         auth_header = authentication.get_authorization_header(request).split()
#         auth_header_prefix = self.authentication_header_prefix.lower()

#         if not auth_header:
#             return None
#         if len(auth_header)==1:
#             return None
#         elif len(auth_header)>2:
#             return None
#         prefix = auth_header[0].decode('utf-8')
#         token = auth_header[1].decode('utf-8')

#         if prefix.lower() != auth_header_prefix:
#             return None
        
#         return self._authenticate_credentials(request, token)
    
#     def _authenticate_credentials(self, request, token):
#         try:
#             payload = jwt.decode(token, settings.SECRET_KEY)
#         except:
#             raise exceptions.AuthenticationFailed("Invalid Authentication. Could not decode Committee token.")

#         try:
#             user = Committee.objects.get(pk=payload['id'])
#         except Committee.DoesNotExist:
#             raise exceptions.AuthenticationFailed("No Committee matching this token was found.")

#         if not user.is_active:
#             raise exceptions.AuthenticationFailed("This User has been deactivated")
        
#         return(user, token)

# class JWTHeadAuthentication(authentication.BaseAuthentication):
#     authentication_header_prefix = 'Token'

#     def authenticate(self, request):
#         request.user = None
#         auth_header = authentication.get_authorization_header(request).split()
#         auth_header_prefix = self.authentication_header_prefix.lower()

#         if not auth_header:
#             return None
#         if len(auth_header)==1:
#             return None
#         elif len(auth_header)>2:
#             return None
#         prefix = auth_header[0].decode('utf-8')
#         token = auth_header[1].decode('utf-8')

#         if prefix.lower() != auth_header_prefix:
#             return None
        
#         return self._authenticate_credentials(request, token)
    
#     def _authenticate_credentials(self, request, token):
#         try:
#             payload = jwt.decode(token, settings.SECRET_KEY)
#         except:
#             raise exceptions.AuthenticationFailed("Invalid Authentication. Could not decode Head token.")

#         try:
#             user = DepartmentHead.objects.get(pk=payload['id'])
#         except DepartmentHead.DoesNotExist:
#             raise exceptions.AuthenticationFailed("No Department Head matching this token was found.")

#         if not user.is_active:
#             raise exceptions.AuthenticationFailed("This User has been deactivated")
        
#         return(user, token)


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

#     def authenticate(self, request):
#         request.user = None
#         auth_header = authentication.get_authorization_header(request).split()
#         auth_header_prefix = self.authentication_header_prefix.lower()

#         if not auth_header:
#             return None
#         if len(auth_header)==1:
#             return None
#         elif len(auth_header)>2:
#             return None
#         prefix = auth_header[0].decode('utf-8')
#         token = auth_header[1].decode('utf-8')

#         if prefix.lower() != auth_header_prefix:
#             return None
        
#         return self._authenticate_credentials(request, token)
    
    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(jwt=token, key="Deez Nuts", algorithms=['HS256'])
        except:
            raise exceptions.AuthenticationFailed("Invalid Authentication. Could not decode token.")

        try:
            user = Teacher.objects.get(pk=payload['id'])
        except Teacher.DoesNotExist:
            print("No Teacher Found for This Shite")

        try:
            user = DepartmentHead.objects.get(pk=payload['id'])
        except DepartmentHead.DoesNotExist:
            print("No Dept Head Found for This Shite")

        try:
            user = Committee.objects.get(pk=payload['id'])
        except Committee.DoesNotExist:
            print("No Committee Found for This Shite")

        if user is None:
            raise User.DoesNotExist("User does not exist")

        if not user.is_active:
            raise exceptions.AuthenticationFailed("This User has been deactivated")
        
#         return(user, token)
