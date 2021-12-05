"""CRUDOperation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users',views.showemp,name="showemp"),
    path('',views.main,name="main"),
    path('Tables',views.tables,name="tables"),
    path('test',views.Test,name="Test"),
    path('query3',views.Query3,name="Query3"),
    path('query2',views.Query2,name="Query2"),
    path('query4',views.Query4,name="Query4"),
    path('query5',views.Query5,name="Query5"),
    path('query6',views.Query6,name="Query6"),
    path('query7',views.Query7,name="Query7"),
    path('query8',views.Query8,name="Query8"),
    path('queries',views.queries,name="queries"),
    path('Country',views.showcountry,name="showcountry"),
    path('Diseasetype',views.showdiseasetype,name="showdiseasetype"),
    path('Disease',views.showdisease,name="showdisease"),
    path('Record',views.showrecord,name="showrecord"),
    path('Doctor',views.showdoctor,name="showdoctor"),
    path('Discover',views.showdiscover,name="showdiscover"),
    path('Specialize',views.showspecialize,name="showspecialize"),
    path('Publicservant',views.showpublicservant,name="showpublicservant"),
    path('Insert',views.Insertemp,name="Insertemp"),
    path('Insertcountry',views.Insertcountry,name="Insertcountry"),
    path('Insertdoctor',views.Insertdoctor,name="Insertdoctor"),
    path('Insertpublicservant',views.Insertpublicservant,name="Insertpublicservant"),
    path('Insertdisease',views.Insertdisease,name="Insertdisease"),
    path('Insertdiseasetype',views.Insertdiseasetype,name="Insertdiseasetype"),
    path('Insertdiscover',views.Insertdiscover,name="Insertdiscover"),
    path('Edit/<str:email>',views.Editemp,name="Editemp"), 
    path('Editcountry/<str:cname>',views.Editcountry,name="Editcountry"), 
    path('Editdisease/<str:disease_code>',views.Editdisease,name="Editdisease"), 
    path('Editdiseasetype/<int:id>',views.Editdiseasetype,name="Editdiseasetype"), 
    path('Editdoctor/<str:email>',views.Editdoctor,name="Editdoctor"), 
    path('Editpublicservant/<str:email>',views.Editpublicservant,name="Editpublicservant"), 
    path('Editdiscover/<str:cname><disease_code>',views.Editdiscover,name="Editdiscover"), 
    path('Update/<str:email>',views.updateemp,name="updateemp"),
    path('Updatecountry/<str:cname>',views.updatecountry,name="updatecountry"),
    path('Updatedisease/<str:disease_code>',views.updatedisease,name="updatedisease"),
    path('Updatediseasetype/<int:id>',views.updatediseasetype,name="updatediseasetype"),
    path('Updatediscover/<str:cname><str:disease_code>',views.updatediscover,name="updatediscover"),
    path('Updatedoctor/<str:email>',views.updatedoctor,name="updatedoctor"),
    path('Updatepublicservant/<str:email>',views.updatepublicservant,name="updatepublicservant"),
    path('Delete/<str:email>',views.Delemp,name="Delemp"),
    path('Deletecountry/<str:cname>',views.Delcountry,name="Delcountry"),
    path('Deletedisease/<str:disease_code>',views.Deldisease,name="Deldisease"),
    path('Deletediseasetype/<int:id>',views.Deldiseasetype,name="Deldiseasetype"),
    path('Deletediscover/<str:cname><str:disease_code>',views.Deldiscover,name="Deldiscover"),
    path('Deletedoctor/<str:email>',views.Deldoctor,name="Deldoctor"),
    path('Deletepublicservant/<str:email>',views.Delpublicservant,name="Delpublicservant"),
]
