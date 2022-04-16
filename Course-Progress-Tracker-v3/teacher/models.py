from datetime import date
import django.dispatch
from django.db import models

from customuser.models import User
from .utils import get_random_id


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, null=True, blank=True)
    teacher_code = models.CharField(max_length=5, primary_key=True)
    is_head = models.BooleanField(default=False)

    def get_code(id):
        return id.split("-")[0].strip()

    def __str__(self):
        return self.teacher_code + " - " + self.name


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

    # class Meta:
    #     unique_together = (
    #         "semester",
    #         "year",
    #     )
    def __str__(self):
        return self.committee_id


class Course(models.Model):
    course_types = [("theory", "Theory"), ("lab", "Lab")]
    course_code = models.CharField(max_length=10, unique=True)
    course_title = models.CharField(max_length=100)
    course_credit = models.FloatField()
    course_type = models.CharField(
        max_length=10, choices=course_types, default="theory"
    )
    teacher = models.ManyToManyField(Teacher)
    committee = models.ForeignKey(
        Committee, on_delete=models.SET_DEFAULT, default="unassigned"
    )
    year = models.CharField(max_length=4, default=date.today().year)

    def __str__(self):
        return self.course_code + "_" + self.year

    class Meta:
        unique_together = (
            "course_code",
            "year",
        )

    def print_all_params(self):
        print(self.course_type)
        print(self.course_code)
        print(self.course_title)
        print(self.course_credit)
        print(self.teacher.all())
        print(self.committee)
        print(self.year)


@django.dispatch.receiver(models.signals.pre_save, sender=Committee)
def set_default_committee_id(sender, instance, *args, **kwargs):
    """
    :param sender: The class that sent the signal.
    :param instance: The instance that is being initialised.
    :return: None.
    """
    instance.committee_id = (
        str(instance.year) + "_" + instance.semester + "_" + get_random_id(10)
    )


class Deadline(models.Model):
    status_tags = [("complete", "Completed"), ("incomplete", "Incomplete")]
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_DEFAULT,
        default="unassigned",
    )
    date = models.DateField(auto_now=False, auto_now_add=False)
    details = models.TextField()
    status = models.CharField(max_length=20, choices=status_tags, default="incomplete")

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return str(self.course) + "_" + str(self.date)
