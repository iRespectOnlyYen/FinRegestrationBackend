from rest_framework import generics
from .models import User, SchoolBoy, Teacher
from .serializers import UserSerializer, SchoolBoySerializer, TeacherSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SchoolBoyCreateView(generics.CreateAPIView):
    queryset = SchoolBoy.objects.all()
    serializer_class = SchoolBoySerializer


class TeacherCreateView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
