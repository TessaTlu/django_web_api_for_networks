from django.shortcuts import render, redirect
from .models import Analysis
from .forms import AnalysisForm
from django.views.generic import DetailView, DeleteView


def patients_home(request):
    analysis = Analysis.objects.order_by('-date')
    return render(request, 'patients/patients.html', {'analysis': analysis})


class PatientsDetail(DetailView):
    model = Analysis
    template_name = 'patients/det.html'
    context_object_name = 'analysis'


class PatientsDelete(DeleteView):
    model = Analysis
    success_url = '/patients/'
    template_name = 'patients/patients_delete.html'


def scan(request):
    error=''
    if request.method == 'POST':
        form = AnalysisForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('home')
        else:
            error='Incorrect form'
    form=AnalysisForm()
    data={
        'form': form,
        'error': error
    }

    return render(request, 'patients/scan.html', data)