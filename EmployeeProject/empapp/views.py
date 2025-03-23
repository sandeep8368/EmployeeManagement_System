from django.shortcuts import render
from empapp.models import empModel

# Create your views here.
def display_view(request):
    emp_data = empModel.objects.all()
    my_dict = {
        'emp':emp_data
    }
    
    return render(request,'html/index.html',my_dict)