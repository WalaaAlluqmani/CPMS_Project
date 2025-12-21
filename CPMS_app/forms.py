from django.forms import ModelForm
from .models import KPI

#we are using this insted of creating another view BECAUSE we want it 
#to be viewd INSID the page, alongside everything else in that page
class KPIForm(ModelForm):
    class Meta():
        model = KPI
        fields = ['kpi', 'unit', 'target_value','actual_value']
