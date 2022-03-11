from rest_framework.serializers import ModelSerializer

from .models import Drug, FormOfRelease, Patient, PrescriptionDrug, Recipe


class FormOfReleaseSerializer(ModelSerializer):
    class Meta:
        model = FormOfRelease
        fields = [
            "name",
        ]

class DrugSerializer(ModelSerializer):
    class Meta:
        model = Drug
        fields = [
            "uuid",
            "name",
            "form_of_release",
            "cost",
            "branch",
            "recipe",
            "indications",
            "storage_conditions",
        ]

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "uuid",
            "first_name",
            "last_name",
            "patronymic",
            "birthday_date",
        ]

class RecipeSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            "patient",
            "recipe_date",
        ]

class PrescriptionDrugSerializer(ModelSerializer):
    class Meta:
        model = PrescriptionDrug
        fields = [
            "name",
            "recipe_id",
            "quantity",
        ]
