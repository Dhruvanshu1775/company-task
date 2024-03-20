from rest_framework import serializers
from .models import Employee, Company


class CompanySerializer(serializers.ModelSerializer):
    class meta:
        model = Company
        fields = ('id','name')

class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), required=False
    )

    class Meta:
        model = Employee
        fields = ('id','first_name','last_name', 'company', 'phone_number','salary','manager_id','department_id')




