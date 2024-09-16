from django.shortcuts import render
from l1.form import L1Form

def index(request):
    form = L1Form()
    return render(request, 'l1/index.html', {'form': form})
