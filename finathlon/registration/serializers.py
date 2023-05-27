from rest_framework import serializers
from .models import Role, User, Teacher, SchoolBoy, Team


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'title', 'url')


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'birth_date', 'birth_place',
                  'live_place', 'index_place', 'phone_number', 'role')

    def create(self, validated_data):
        role_data = validated_data.pop('role')
        role = Role.objects.create(**role_data)
        user = User.objects.create(role=role, **validated_data)
        return user


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ('id', 'user', 'organization', 'post', 'position_type', 'post_index',
                  'work_sector', 'start_year', 'university_title', 'end_year', 'rank', 'education_type')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher


class SchoolBoySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = SchoolBoy
        fields = ('id', 'user', 'school_index', 'title', 'class_level', 'orphan_status', 'disability')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        schoolboy = SchoolBoy.objects.create(user=user, **validated_data)
        return schoolboy


class TeamSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    students = SchoolBoySerializer(many=True)

    class Meta:
        model = Team
        fields = ('id', 'teacher', 'students')

    def create(self, validated_data):
        teacher_data = validated_data.pop('teacher')
        teacher_serializer = TeacherSerializer(data=teacher_data)
        teacher_serializer.is_valid(raise_exception=True)
        teacher = teacher_serializer.save()

        students_data = validated_data.pop('students')
        student_serializer = SchoolBoySerializer(data=students_data, many=True)
        student_serializer.is_valid(raise_exception=True)
        students = student_serializer.save()

        team = Team.objects.create(teacher=teacher)
        team.students.set(students)
        return team
