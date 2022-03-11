"""pharmacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drugsapp.views import (DrugModelViewSet, FormOfReleaseModelViewSet,
                            PatientModelViewSet, PrescriptionDrugModelViewSet,
                            RecipeModelViewSet)
from employeeapp.views import (BranchModelViewSet, PositionModelViewSet,
                               SalaryModelViewSet, StaffModelViewSet,
                               VacationModelViewSet)
from rest_framework.routers import DefaultRouter
from supplyapp.views import (SuppliedDrugModelViewSet, SupplierModelViewSet,
                             SupplyModelViewSet)

router = DefaultRouter()
router.register("Staff", StaffModelViewSet)
router.register("Position", PositionModelViewSet)
router.register("Branch", BranchModelViewSet)
router.register("Vacation", VacationModelViewSet)
router.register("Salary", SalaryModelViewSet)
router.register("Drug", DrugModelViewSet)
router.register("FormOfRelease", FormOfReleaseModelViewSet)
router.register("Patient", PatientModelViewSet)
router.register("PrescriptionDrug", PrescriptionDrugModelViewSet)
router.register("Recipe", RecipeModelViewSet)
router.register("SuppliedDrug", SuppliedDrugModelViewSet)
router.register("Supplier", SupplierModelViewSet)
router.register("Supply", SupplyModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include(router.urls)),
]
