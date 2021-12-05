from enum import unique
from typing import ContextManager
from django import db
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
from django.db.models.fields.related import ForeignKey 

class EmpModel(models.Model): 
    email=models.CharField(max_length=60,primary_key=True)
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=40)
    salary=models.IntegerField()
    phone=models.CharField(max_length=20)
    cname=models.CharField(max_length=50)
    class Meta:
        db_table="users"

class EmpCountry(models.Model): 
    cname=models.CharField(max_length=50,primary_key=True)
    population=models.IntegerField()
    class Meta:
        db_table="country"

class EmpDoctor(models.Model): 
    email=models.CharField(max_length=60,primary_key=True)
    degree=models.CharField(max_length=20)
    class Meta:
        db_table="doctor"

class EmpPublicservant(models.Model): 
    email=models.CharField(max_length=60,primary_key=True)
    department=models.CharField(max_length=50)
    class Meta:
        db_table="publicservant"
    
class EmpDiseasetype(models.Model): 
    id=models.IntegerField(primary_key=True)
    description=models.CharField(max_length=140)
    class Meta:
        db_table="diseasetype"

class EmpSpecialize(models.Model): 
    specid = models.IntegerField(primary_key=True, unique=True)
    id=models.ForeignKey(EmpDiseasetype, db_column='id',on_delete=models.CASCADE,related_name='spid')
    email=models.ForeignKey(EmpModel, db_column='email', on_delete=models.CASCADE, related_name='spemai')
    class Meta:
        db_table="specialize"
        unique_together=(('id','email'),)

class EmpDisease(models.Model): 
    disease_code=models.CharField(max_length=50,primary_key=True)
    pathogen=models.CharField(max_length=20)
    description=models.CharField(max_length=140)
    id=models.IntegerField()
    class Meta:
        db_table="disease"

class EmpDiscover(models.Model): 
    cname=models.CharField(max_length=50,primary_key=True)
    disease_code=models.CharField(max_length=50)
    first_enc_date=models.DateField()
    class Meta:
        db_table="discover"

class EmpRecord(models.Model): 
    cname=models.CharField(max_length=50,primary_key=True)
    email=models.CharField(max_length=60)
    disease_code=models.CharField(max_length=50)
    class Meta:
        db_table="record"
        unique_together=(('cname','email','disease_code'),)