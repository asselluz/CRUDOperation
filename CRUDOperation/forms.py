from django import forms
from CRUDOperation.models import EmpCountry 
from CRUDOperation.models import EmpModel
from CRUDOperation.models import EmpCountry
from CRUDOperation.models import EmpDiscover
from CRUDOperation.models import EmpDisease
from CRUDOperation.models import EmpDiseasetype
from CRUDOperation.models import EmpDoctor
from CRUDOperation.models import EmpPublicservant
from CRUDOperation.models import EmpSpecialize
from CRUDOperation.models import EmpRecord
class Empforms(forms.ModelForm):
    class Meta:
        model=EmpModel
        fields="__all__"
class Empcountry(forms.ModelForm):
    class Meta:
        model=EmpCountry
        fields="__all__"
class Empdiscover(forms.ModelForm):
    class Meta:
        model=EmpDiscover
        fields="__all__"
class Empdisease(forms.ModelForm):
    class Meta:
        model=EmpDisease
        fields="__all__"
class Empdiseasetype(forms.ModelForm):
    class Meta:
        model=EmpDiseasetype
        fields="__all__"
class Empdoctor(forms.ModelForm):
    class Meta:
        model=EmpDoctor
        fields="__all__"
class Emppublicservant(forms.ModelForm):
    class Meta:
        model=EmpPublicservant
        fields="__all__"
class Empspecizalie(forms.ModelForm):
    class Meta:
        model=EmpSpecialize
        fields="__all__"
class Emprecord(forms.ModelForm):
    class Meta:
        model=EmpRecord
        fields="__all__"