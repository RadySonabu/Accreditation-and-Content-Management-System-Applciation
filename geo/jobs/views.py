from django.shortcuts import render
from .forms import BuyerA00Form,BuyerA01Form,BuyerA02Form,BuyerA03Form
# Create your views here.
def job(request):
    context = {
        
    }
    return render(request, 'jobs/job-job.html', context)


