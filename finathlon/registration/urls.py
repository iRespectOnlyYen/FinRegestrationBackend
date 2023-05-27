from django.urls import path
from .views import UserCreateView, SchoolBoyCreateView, TeacherCreateView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('schoolboys/', SchoolBoyCreateView.as_view(), name='schoolboy-create'),
    path('teachers/', TeacherCreateView.as_view(), name='teacher-create'),
]