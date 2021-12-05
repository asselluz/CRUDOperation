from django.core.checks import messages
from django.shortcuts import render
from CRUDOperation.models import EmpRecord
from CRUDOperation.forms import Empdiscover
from CRUDOperation.models import EmpDiscover
from CRUDOperation.models import EmpCountry 
from CRUDOperation.models import EmpModel 
from CRUDOperation.models import EmpDisease
from CRUDOperation.models import EmpDiseasetype
from CRUDOperation.models import EmpDoctor
from CRUDOperation.models import EmpPublicservant
from CRUDOperation.models import EmpSpecialize
from django.contrib import messages
from CRUDOperation.forms import Empforms
from CRUDOperation.forms import Empcountry
from CRUDOperation.forms import Empdisease
from CRUDOperation.forms import Empdiseasetype
from CRUDOperation.forms import Empdoctor
from CRUDOperation.forms import Emppublicservant
from CRUDOperation.forms import Empspecizalie
from CRUDOperation.forms import Emprecord

def showemp(request):
    showall=EmpModel.objects.all()
    return render(request,'Index.html',{"data":showall})

def main(request):
    return render(request,'main.html', )

def tables(request):
    return render(request,'Tables.html', )

def queries(request):
    return render(request,'queries.html', )

def showdisease(request):
    showall=EmpDisease.objects.all()
    return render(request,'Disease.html',{"data":showall})

def showdiseasetype(request):
    showall=EmpDiseasetype.objects.all()
    return render(request,'Diseasetype.html',{"data":showall})

def showdoctor(request):
    showall=EmpDoctor.objects.all()
    return render(request,'Doctor.html',{"data":showall})

def showpublicservant(request):
    showall=EmpPublicservant.objects.all()
    return render(request,'Publicservant.html',{"data":showall})

def showspecialize(request):
    showall=EmpSpecialize.objects.all()
    return render(request,'Specialize.html',{"data":showall})

def showrecord(request):
    showall=EmpRecord.objects.all()
    return render(request,'Record.html',{"data":showall})

def Editemp(request,email):
    editempobj=EmpModel.objects.get(email=email)
    return render(request,'Edit.html',{"EmpModel":editempobj})

def updateemp(request,email):
    Updateemp=EmpModel.objects.get(email=email)
    form=Empforms(request.POST,instance=Updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully!")
        return render(request,'Edit.html',{"EmpModel":Updateemp})
    
def Editdisease(request,disease_code):
    editdiseaseobj=EmpDisease.objects.get(disease_code=disease_code)
    return render(request,'Editdisease.html',{"EmpDisease":editdiseaseobj})

def updatedisease(request,disease_code):
    Updatedisease=EmpDisease.objects.get(disease_code=disease_code)
    form=Empdisease(request.POST,instance=Updatedisease)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully!")
        return render(request,'Editdisease.html',{"EmpDisease":Updatedisease})

def Editdiseasetype(request,id):
    editdiseasetypeobj=EmpDiseasetype.objects.get(id=id)
    return render(request,'Editdiseasetype.html',{"EmpDiseasetype":editdiseasetypeobj})

def updatediseasetype(request,id):
    Updatediseasetype=EmpDiseasetype.objects.get(id=id)
    form=Empdiseasetype(request.POST,instance=Updatediseasetype)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully!")
        return render(request,'Editdiseasetype.html',{"EmpDisease":Updatediseasetype})

def showcountry(request):
    showall=EmpCountry.objects.all()
    return render(request,'Country.html',{"data":showall})

def showdiscover(request):
    showall=EmpDiscover.objects.all()
    return render(request,'Discover.html',{"data":showall})

def Insertemp(request):
    if request.method=="POST":
        if request.POST.get('email') and request.POST.get('name') and request.POST.get('surname') and request.POST.get('salary') and request.POST.get('phone') and request.POST.get('cname'):
            saverecord=EmpModel()
            saverecord.email=request.POST.get('email')
            saverecord.name=request.POST.get('name')
            saverecord.surname=request.POST.get('surname')
            saverecord.salary=request.POST.get('salary')
            saverecord.phone=request.POST.get('phone')
            saverecord.cname=request.POST.get('cname')
            saverecord.save()
            messages.success(request,'User '+saverecord.name+ ' is saved successfully..!')
            return render(request,'Insert.html') 
    else:
            return render(request,'Insert.html')

def Insertcountry(request):
    if request.method=="POST":
        if request.POST.get('cname') and request.POST.get('population'):
            saverecord=EmpCountry()
            saverecord.cname=request.POST.get('cname')
            saverecord.population=request.POST.get('population')
            saverecord.save()
            messages.success(request,'Country '+saverecord.cname+ ' is saved successfully..!')
            return render(request,'Insertcountry.html') 
    else:
            return render(request,'Insertcountry.html')

def Insertdisease(request):
    if request.method=="POST":
        if request.POST.get('disease_code') and request.POST.get('pathogen') and request.POST.get('description') and request.POST.get('id'):
            saverecord=EmpDisease()
            saverecord.disease_code=request.POST.get('disease_code')
            saverecord.pathogen=request.POST.get('pathogen')
            saverecord.description=request.POST.get('description')
            saverecord.id=request.POST.get('id')
            saverecord.save()
            messages.success(request,'Disease '+saverecord.disease_code+ ' is saved successfully..!')
            return render(request,'Insertdisease.html') 
    else:
            return render(request,'Insertdisease.html')

def Insertdiseasetype(request):
    if request.method=="POST":
        if request.POST.get('id') and request.POST.get('description'):
            saverecord=EmpDiseasetype()
            saverecord.id=request.POST.get('id')
            saverecord.description=request.POST.get('description')
            saverecord.save()
            messages.success(request,'Disease type'+saverecord.id+ ' is saved successfully..!')
            return render(request,'Insertdiseasetype.html') 
    else:
            return render(request,'Insertdiseasetype.html')

def Insertdiscover(request):
    if request.method=="POST":
        if request.POST.get('cname') and request.POST.get('disease_code') and request.POST.get('first_enc_date'):
            saverecord=EmpDiscover()
            saverecord.cname=request.POST.get('cname')
            saverecord.disease_code=request.POST.get('disease_code')
            saverecord.first_enc_date=request.POST.get('first_enc_date')
            saverecord.save()
            messages.success(request,'New discover in '+saverecord.cname+ ' is saved successfully..!')
            return render(request,'Insertdiscover.html') 
    else:
            return render(request,'Insertdiscover.html')

def Insertdoctor(request):
    if request.method=="POST":
        if request.POST.get('email') and request.POST.get('degree'):
            saverecord=EmpDoctor()
            saverecord.email=request.POST.get('email')
            saverecord.degree=request.POST.get('degree')
            saverecord.save()
            messages.success(request,'New doctor in '+saverecord.email+ ' is saved successfully..!')
            return render(request,'Insertdoctor.html') 
    else:
            return render(request,'Insertdoctor.html')

def Insertpublicservant(request):
    if request.method=="POST":
        if request.POST.get('email') and request.POST.get('department'):
            saverecord=EmpPublicservant()
            saverecord.email=request.POST.get('email')
            saverecord.department=request.POST.get('department')
            saverecord.save()
            messages.success(request,'New public servant in '+saverecord.email+ ' is saved successfully..!')
            return render(request,'Insertpublicservant.html') 
    else:
            return render(request,'Insertpublicservant.html')

def Editcountry(request,cname):
    editempcountry=EmpCountry.objects.get(cname=cname)
    return render(request,'Editcountry.html',{"EmpCountry":editempcountry})

def updatecountry(request,cname):
    Updatecountry=EmpCountry.objects.get(cname=cname)
    form=Empcountry(request.POST,instance=Updatecountry)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully!")
        return render(request,'Editcountry.html',{"EmpCountry":Updatecountry})

def Editdoctor(request,email):
    editempdoctor=EmpDoctor.objects.get(email=email)
    return render(request,'Editdoctor.html',{"EmpDoctor":editempdoctor})

def updatedoctor(request,email):
    Updatedoctor=EmpDoctor.objects.get(email=email)
    form=Empdoctor(request.POST,instance=Updatedoctor)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully!")
        return render(request,'Editdoctor.html',{"EmpDoctor":Updatedoctor})

def Editpublicservant(request,email):
    editpublicservant=EmpPublicservant.objects.get(email=email)
    return render(request,'Editpublicservant.html',{"EmpPublicservant":editpublicservant})

def updatepublicservant(request,email):
    Updatepublicservant=EmpPublicservant.objects.get(email=email)
    form=Emppublicservant(request.POST,instance=Updatepublicservant)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully!")
        return render(request,'Editpublicservant.html',{"EmpPublicservant":Updatepublicservant})

def Editdiscover(request,cname,disease_code):
    editempdiscover=EmpDiscover.objects.filter(cname=cname,disease_code=disease_code)
    return render(request,'Editdiscover.html',{"EmpDiscover":editempdiscover})

def updatediscover(request,cname,disease_code):
    Updatediscover=EmpDiscover.objects.filter(cname=cname,disease_code=disease_code)
    form=EmpDiscover(request.POST,instance=Updatediscover)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully!")
        return render(request,'Editdiscover.html',{"EmpDiscover":Updatediscover})

def Delemp(request,email):
    deluser=EmpModel.objects.get(email=email)
    deluser.delete()
    showdata=EmpModel.objects.all()
    return render(request,"Index.html",{"data":showdata})

def Delcountry(request,cname):
    delcountry=EmpCountry.objects.get(cname=cname)
    delcountry.delete()
    showdata=EmpCountry.objects.all()
    return render(request,"Country.html",{"data":showdata})

def Deldiseasetype(request,id):
    deldiseasetype= EmpDiseasetype.objects.get(id=id)
    deldiseasetype.delete()
    showdata=EmpDiseasetype.objects.all()
    return render(request,"Diseasetype.html",{"data":showdata})

def Deldisease(request,disease_code):
    deldisease= EmpDisease.objects.get(disease_code=disease_code)
    deldisease.delete()
    showdata=EmpDisease.objects.all()
    return render(request,"Disease.html",{"data":showdata})

def Deldiscover(request,cname,disease_code):
    deldiscover= EmpDiscover.objects.get(cname=cname,disease_code=disease_code)
    deldiscover.delete()
    showdata=EmpDiscover.objects.all()
    return render(request,"Doctor.html",{"data":showdata})

def Deldoctor(request,email):
    deldoctor= EmpDoctor.objects.get(email=email)
    deldoctor.delete()
    showdata=EmpDoctor.objects.all()
    return render(request,"Doctor.html",{"data":showdata})

def Delpublicservant(request,email):
    delpublicservant= EmpPublicservant.objects.get(email=email)
    delpublicservant.delete()
    showdata=EmpPublicservant.objects.all()
    return render(request,"Publicservant.html",{"data":showdata})

def Test(request) :
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("SELECT Disease.disease_code, Disease.description\
                            FROM Disease INNER JOIN Discover ON Disease.disease_code=Discover.disease_code\
                            WHERE pathogen = 'bacteria' AND first_enc_date<'1990-01-01'")
    row = cursor.fetchall()
    context = {"row":row}
    return render(request, "test.html", context)

def Query2(request) :
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT name, surname, degree\
                            FROM Doctor INNER JOIN Specialize ON Doctor.email=Specialize.email\
                            INNER JOIN Users ON Doctor.email=Users.email\
                            INNER JOIN DiseaseType ON Specialize.id=DiseaseType.id\
                            WHERE NOT DiseaseType.Description='infectious diseases'\
                            EXCEPT\
                            SELECT DISTINCT name, surname, degree\
                            FROM Doctor INNER JOIN Specialize ON Doctor.email=Specialize.email\
                            INNER JOIN Users ON Doctor.email=Users.email\
                            INNER JOIN DiseaseType ON Specialize.id=DiseaseType.id\
                            WHERE DiseaseType.Description='infectious diseases'")
    row = cursor.fetchall()
    context = {"row":row}
    return render(request, "query2.html", context)

def Query3(request) :
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("SELECT Users.name, Users.surname, Doctor.degree\
                            FROM Specialize, Users, Doctor\
                            WHERE Users.email=Specialize.email AND Specialize.email=Doctor.email\
                            GROUP BY Specialize.email, Users.email, Doctor.email\
                            HAVING COUNT(*)>2")
    row = cursor.fetchall()
    context = {"row":row}
    return render(request, "query3.html", context)

def Query4(request) :
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("SELECT Country.cname, CAST(AVG(salary) as integer)\
                            FROM  Specialize INNER JOIN DiseaseType ON Specialize.id=DiseaseType.id\
                            INNER JOIN Users ON Specialize.email=Users.email\
                            AND DiseaseType.description='virology' RIGHT OUTER JOIN Country on Users.cname=Country.cname\
                            GROUP BY Country.cname")
    row = cursor.fetchall()
    context = {"row":row}
    return render(request, "query4.html", context)

def Query5(request) :
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("SELECT department, count(*) FROM PublicServant,\
                            (SELECT disease_code, email, COUNT(*) FROM\
                            Record GROUP BY disease_code,email HAVING COUNT(disease_code='COVID-19')>1)\
                            AS t1 WHERE t1.email=PublicServant.email GROUP BY department")
    row = cursor.fetchall()
    context = {"row":row}
    return render(request, "query5.html", context)

def Query6(request) :
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT Users.email, name, department FROM\
                            Record INNER JOIN PublicServant ON Record.email=PublicServant.email\
                            INNER JOIN Users ON PublicServant.email=Users.email\
                            WHERE Record.total_patients BETWEEN 100000 AND 999999")  
    row = cursor.fetchall()
    context = {"row":row}
    return render(request, "query6.html", context)

def Query7(request) :
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("SELECT cname, SUM(total_patients) AS tpatients\
                            FROM Record GROUP BY cname ORDER BY SUM(total_patients) DESC LIMIT 5;")  
    row = cursor.fetchall()
    context = {"row":row}
    return render(request, "query7.html", context)

def Query8(request) :
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("SELECT DiseaseType.description, COALESCE(SUM(total_patients),0) AS tpatients FROM\
                            Record RIGHT JOIN Disease ON Disease.disease_code=Record.disease_code\
                            RIGHT JOIN DiseaseType ON Disease.id=DiseaseType.id\
                            GROUP BY DiseaseType.description")  
    row = cursor.fetchall()
    context = {"row":row}
    return render(request, "query8.html", context)

