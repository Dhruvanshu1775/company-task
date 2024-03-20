from django.shortcuts import render
import csv
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilizers import EmployeeSerializer
from .models import Company, Employee


class UploadCSV(APIView):
    def post(self, request):
        file = request.FILES['file']
        read = pd.read_excel(file)

        employee_data_list = []
        for index, row in read.iterrows():
            company, created = Company.objects.get_or_create(name=row[4])
            phone_number = row[3].replace('.','') 
            employee_data = {
                'id': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'phone_number':phone_number,
                'company':int(company.id),
                'salary': int(row[5]),
                'manager_id':int(row[6]),
                'department_id':int(row[7]),
            }
            
            serializer = EmployeeSerializer(data=employee_data)
            if serializer.is_valid():
                employee_data_list.append(employee_data)
            else:
                return Response(serializer.errors, status=400)
        return Response({'message': 'Data uploaded successfully','employees':employee_data_list}, status=200)
    
    def get(self, request):
        employee_obj = Employee.objects.all().select_related('company')
        serializer = EmployeeSerializer(instance=employee_obj, many=True)
        return Response(serializer.data, status=200)
