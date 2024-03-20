from django.db import models

# Create your models here.

class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(DateTimeMixin):
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name


class Employee(DateTimeMixin):
    company = models.ForeignKey(Company,on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.FloatField()
    salary = models.IntegerField()
    manager_id = models.IntegerField()
    department_id = models.IntegerField()

    def __str__(self) -> str:
        return (self.first_name + " " + self.last_name)




