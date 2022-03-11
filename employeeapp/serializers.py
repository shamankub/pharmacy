from rest_framework.serializers import ModelSerializer

from .models import Branch, Position, Salary, Staff, Vacation


class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = [
            "uuid",
            "first_name",
            "last_name",
            "patronymic",
            "passport_num",
            "passport_date",
            "address",
            "phone",
            "email",
            "branch",
            "position",
        ]

class PostionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = [
            "name",
            "experience",
            "salary",
        ]

class BranchSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = [
            "name",
            "branch_head",
            "address",
            "phone",
        ]

class VacationSerializer(ModelSerializer):
    class Meta:
        model = Vacation
        fields = [
            "staff_id",
            "vacation_start",
            "vacation_end",
        ]

class SalarySerializer(ModelSerializer):
    class Meta:
        model = Salary
        fields = [
            "staff_id",
            "salary_date",
            "salary",
            "salary_bonus",
        ]
