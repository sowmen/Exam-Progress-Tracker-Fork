# from re import S
# from django.conf import settings
# import jwt
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.db import models
# from django.contrib.auth.models import PermissionsMixin
# import uuid, datetime
# from typing import Type
# from django.contrib.auth.base_user import BaseUserManager

# from django.utils import tree


# class UserManager(BaseUserManager):
#     def get_by_natural_key(self, email):
#         return self.get(email=email)

#     def create_user(self, email, password=None):
#         if email is None:
#             raise TypeError("Users must have an email address.")

#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save()

#         return user

#     def create_superuser(self, email, password):
#         if password is None:
#             raise TypeError("Superusers must have a password.")

#         user = self.create_user(email, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()

#         return user


# class TeacherManager(BaseUserManager):
#     def create_teacher(
#         self, first_name, last_name, email, initials, created_by, password=None
#     ):
#         if email is None:
#             raise TypeError("Users must have an email address.")
#         teacher = Teacher(
#             self,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             initials=initials,
#             created_by=created_by,
#             user_type="TCHR",
#         )
#         teacher.set_password(password)
#         teacher.save()
#         return teacher


# class CommitteeManager(BaseUserManager):
#     def create_committee(
#         self, email, id, session, external, created_by, members, password=None
#     ):
#         if email is None:
#             raise TypeError("Users must have an email address.")
#         committee = Committee(
#             self,
#             id=id,
#             email=email,
#             session=session,
#             external=external,
#             created_by=created_by,
#             members=members,
#             user_type="CMTE",
#         )
#         committee.set_password(password)
#         committee.save()
#         return committee


# class HeadManager(BaseUserManager):
#     def create_head(self, email, initials, first_name, last_name, password=None):
#         if email is None:
#             raise TypeError("Users must have an email address.")
#         head = DepartmentHead(
#             self,
#             email=email,
#             initials=initials,
#             first_name=first_name,
#             last_name=last_name,
#             user_type="HEAD",
#         )
#         head.set_password(password)
#         head.save()
#         return head


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(db_index=True, primary_key=True)
#     user_type = models.CharField(blank=True, default="SuperAdmin", max_length=6)
#     first_name = models.CharField(max_length=100, default=None, null=True, blank=True)
#     last_name = models.CharField(max_length=100, default=None, null=True, blank=True)

#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     USERNAME_FIELD = "email"

#     objects = UserManager()

#     @property
#     def token(self):
#         dt = datetime.datetime.now() + datetime.timedelta(days=60)
#         token = jwt.encode(
#             {"id": self.pk, "exp": int(dt.strftime("%s"))},
#             "Deez Nuts",
#             algorithm="HS256",
#         )
#         return token

#     def __str__(self):
#         return self.email


# class DepartmentHead(User, PermissionsMixin):

#     initials = models.CharField(blank=False, max_length=3)

#     USERNAME_FIELD = "email"

#     objects = HeadManager()


# class Teacher(User, PermissionsMixin):

#     initials = models.CharField(blank=False, max_length=3, unique=True)
#     created_by = models.ForeignKey(DepartmentHead, on_delete=models.DO_NOTHING)

#     USERNAME_FIELD = "email"

#     objects = TeacherManager()

#     def __str__(self):
#         return self.initials


# class Committee(User, PermissionsMixin):

#     id = models.CharField(blank=False, max_length=50, unique=True)
#     session = models.CharField(blank=False, max_length=20)
#     external = models.CharField(blank=True, max_length=50)
#     created_by = models.OneToOneField(DepartmentHead, on_delete=models.CASCADE)
#     members = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

#     USERNAME_FIELD = "email"

#     objects = CommitteeManager()


# ################################################################################################################################################################################################################################################################################################################################################################################################################


# class Message(models.Model):

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     sent_from = models.ForeignKey(
#         User, on_delete=models.DO_NOTHING, related_name="sender"
#     )
#     sent_to = models.ForeignKey(
#         User, on_delete=models.DO_NOTHING, related_name="receiver"
#     )
#     sent_date = models.DateTimeField(auto_now=True, blank=True)
#     data = models.CharField(blank=True, max_length=200)


# class Course(models.Model):
#     course_code = models.CharField(unique=True, max_length=20)
#     USN = models.CharField(primary_key=True, max_length=30)
#     year = models.IntegerField(default=2021)
#     session = models.CharField(blank=False, max_length=20)
#     attendees = models.IntegerField(blank=False)


# class Deadlines(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     details = models.CharField(blank=False, max_length=500)
#     deadline_for = models.ForeignKey(User, on_delete=models.CASCADE)
#     deadline = models.DateTimeField()
