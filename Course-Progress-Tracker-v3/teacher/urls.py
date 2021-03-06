from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.teacher_home, name='teacher_home'),
    path('courses', views.teacher_course, name='teacher_course'),
    path('committee', views.teacher_committee, name='teacher_committee'),
    path('head', views.teacher_head, name='teacher_head'),
    path('create_course', views.create_course, name='teacher_create_course'),
    path('create_deadline', views.create_deadline, name='teacher_create_deadline'),
    path('create_committee', views.create_committee, name='teacher_create_committee'),
    path('edit_deadlines', views.edit_deadline, name="committee_edit_deadline"),

    # path('createsession/', views.createsession, name='createsession'),
    # path('<str:session_id>/', views.batchinfo, name='batchinfo'),
    # path('<str:session_id>/<str:project_id>/', views.projectdetails, name='projectdetails'),
]
