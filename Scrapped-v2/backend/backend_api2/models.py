from django import utils
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone
from datetime import date
from .utils import get_random_id

from django.db import models
import django.dispatch


########################## Define CustomUser using email address ######################
class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, primary_key=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % self.pk

    def get_email(self):
        return self.email

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email


#########################################################################


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    initials = models.CharField(max_length=5, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    is_dept_head = models.BooleanField(default=False)

    def __str__(self):
        return self.initials

    def __unicode__(self):
        return self.initials


class Committee(models.Model):
    session_options = [
        ("1/1", "1/1"),
        ("1/2", "1/2"),
        ("2/1", "2/1"),
        ("2/2", "2/2"),
        ("3/1", "3/1"),
        ("3/2", "3/2"),
        ("4/1", "4/1"),
        ("4/2", "4/2"),
    ]
    year = models.CharField(max_length=4, default=date.today().year)
    semester = models.CharField(max_length=10, choices=session_options, default="1/1")
    committee_id = models.CharField(max_length=250, primary_key=True, editable=False)
    teachers = models.ManyToManyField(Teacher)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.committee_id


@django.dispatch.receiver(models.signals.pre_save, sender=Committee)
def set_default_committee_id(sender, instance, *args, **kwargs):
    """
    Set the default value for `subject_initials` on the `instance`.

    :param sender: The `LoremIpsum` class that sent the signal.
    :param instance: The `LoremIpsum` instance that is being
        initialised.
    :return: None.
    """
    instance.committee_id = (
        str(instance.year) + "_" + instance.semester + "_" + get_random_id(10)
    )


class Course(models.Model):
    course_types = [("theory", "Theory"), ("lab", "Lab")]
    course_code = models.CharField(max_length=10, primary_key=True)
    course_title = models.CharField(max_length=100)
    course_credit = models.FloatField()
    course_type = models.CharField(
        max_length=10, choices=course_types, default="Theory"
    )
    session = models.CharField(max_length=250)

    committee_code = models.ForeignKey(
        Committee, on_delete=models.SET_DEFAULT, default="unassigned"
    )
    teacher_code = models.ForeignKey(
        Teacher, on_delete=models.SET_DEFAULT, default="unassigned"
    )

    def __str__(self):
        return self.course_code + "-" + self.course_title


class Deadline(models.Model):
    status_tags = [("complete", "Completed"), ("incomplete", "Incomplete")]
    course_code = models.ForeignKey(
        Course,
        blank=True,
        null=True,
        on_delete=models.SET_DEFAULT,
        default="unassigned",
    )
    committee_deadline = models.ForeignKey(
        Committee,
        blank=True,
        null=True,
        on_delete=models.SET_DEFAULT,
        default="unassigned",
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_DEFAULT, default="unassigned"
    )
    date = models.DateField(auto_now=False, auto_now_add=False)
    details = models.TextField(null=True)
    status = models.CharField(max_length=20, choices=status_tags, default="incomplete")

    class Meta:
        ordering = ("date",)

    def __str__(self):
        return str(self.date)
