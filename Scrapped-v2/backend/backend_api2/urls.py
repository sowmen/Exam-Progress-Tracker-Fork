from backend_api2.views import (
    TeacherList,
    TeacherCreate,
    TeacherDetail,
    # UserDetail,
)
from django.urls import path, include

# from .views import CommitteeCreate, HeadCreate, TeacherCreate, UserLogin, HelloWorld

urlpatterns = [
    # path("user/create/committee/", CommitteeCreate.as_view(), name="create_committee"),
    # path("user/create/teacher/", TeacherCreate.as_view(), name="create_teacher"),
    # path("user/create/head/", HeadCreate.as_view(), name="create_head"),
    # path("user/login/", UserLogin.as_view(), name="login"),
    # path("user/hello/", HelloWorld.as_view(), name="test"),
    path("teachers/", TeacherList.as_view(), name="teacher_list_retrieve"),
    path("teachers/create", TeacherCreate.as_view(), name="teacher_create"),
    path("teachers/<str:pk>", TeacherDetail.as_view(), name="teacher_detail_retrieve"),
    # path("users/<str:pk>", UserDetail.as_view(), name="user_detail_retrieve"),
    path("deadline/", TeacherList.as_view(), name="teacher_list_retrieve"),
]
