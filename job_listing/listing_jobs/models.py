from django.db import models

# Create your models here.


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    employee_headline = models.CharField(max_length=255)
    employee_location = models.CharField(max_length=255)
    employee_followers = models.IntegerField()
    employee_connections = models.IntegerField()
    employee_education = models.CharField(max_length=255)
    experience_id = models.ForeignKey('Experience', on_delete=models.CASCADE)
    
    
class Experience(models.Model):
    id = models.IntegerField(primary_key=True)
    duration = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
    
class Source(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
       return str(self.id)
  
class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=255)
    company_website = models.URLField()
    company_address = models.TextField()
    company_contact = models.CharField(max_length=255)
    source_id = models.ForeignKey('Source', on_delete=models.CASCADE)
    def __str__(self):
       return str(self.id)
    
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField()
    
class JobListing(models.Model):
    id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    date_job_post = models.DateField(null=True)
    job_description = models.CharField(max_length=255)
    date_of_scrap = models.DateField(null=True)
    job_id = models.IntegerField(null=True)
    # source_id = models.ForeignKey('Source', on_delete=models.CASCADE)
    # company_id = models.ForeignKey('Company', on_delete=models.CASCADE)
